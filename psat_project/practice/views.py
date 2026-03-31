import random
import json
from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils import timezone
from django.db.models import Avg, Count, Sum

from .models import Subject, Question, TestAttempt, TestQuestion


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _build_test_questions(subject, n, user=None):
    """
    Pull n questions balanced by difficulty: 20% easy / 40% medium / 40% hard.

    Priority order:
      1. Questions the user has NOT seen in their last 20 completed attempts.
      2. Questions from older attempts (seen 20+ attempts ago) — the "mix" phase.

    This ensures no question repeats for the first ~(pool_size / n) attempts,
    then gradually recycles oldest-seen questions.
    """
    # Collect question IDs seen in the user's last 10 completed attempts
    seen_ids = set()
    if user:
        recent = TestAttempt.objects.filter(
            user=user, subject=subject,
            status__in=['submitted', 'timed_out']
        ).order_by('-submitted_at')[:20]
        if recent.exists():
            seen_ids = set(
                TestQuestion.objects.filter(
                    test_attempt__in=recent
                ).values_list('question_id', flat=True)
            )

    all_active = Question.objects.filter(subject=subject, active=True)
    fresh = all_active.exclude(id__in=seen_ids)   # not seen recently
    stale = all_active.filter(id__in=seen_ids)     # seen in last 10 attempts

    n_easy = max(1, round(n * 0.20))
    n_med  = max(1, round(n * 0.40))
    n_hard = n - n_easy - n_med

    def _pick(qs, diff, count):
        pool = list(qs.filter(difficulty=diff))
        random.shuffle(pool)
        return pool[:count]

    # Build from fresh questions first
    selected = (
        _pick(fresh, 'easy',   n_easy) +
        _pick(fresh, 'medium', n_med)  +
        _pick(fresh, 'hard',   n_hard)
    )

    # Fill any shortfall from stale (oldest-seen) questions
    if len(selected) < n:
        used_ids = {q.pk for q in selected}
        fallback = list(stale.exclude(id__in=used_ids))
        random.shuffle(fallback)
        for q in fallback:
            selected.append(q)
            if len(selected) >= n:
                break

    # Last resort: any remaining active question
    if len(selected) < n:
        used_ids = {q.pk for q in selected}
        for q in list(all_active.exclude(id__in=used_ids)):
            selected.append(q)
            if len(selected) >= n:
                break

    random.shuffle(selected)
    return selected[:n]


# ---------------------------------------------------------------------------
# Views
# ---------------------------------------------------------------------------

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('pending_approvals')
    subjects = Subject.objects.all()
    all_attempts = TestAttempt.objects.filter(
        user=request.user, status__in=['submitted', 'timed_out']
    ).select_related('subject')

    # Stats per subject (filter on unsliced queryset)
    stats = {}
    for subject in subjects:
        subject_attempts = all_attempts.filter(subject=subject)
        stats[subject.slug] = {
            'total': subject_attempts.count(),
            'avg_score': subject_attempts.aggregate(a=Avg('score'))['a'],
            'avg_accuracy': subject_attempts.aggregate(a=Avg('accuracy'))['a'],
        }

    # Last 10 attempts for the table and chart
    attempts = all_attempts[:10]

    # Chart data: last 10 attempts scores
    chart_labels = []
    chart_scores = []
    for a in reversed(list(attempts)):
        chart_labels.append(a.started_at.strftime('%b %d'))
        chart_scores.append(a.score or 0)

    return render(request, 'practice/dashboard.html', {
        'subjects': subjects,
        'attempts': attempts,
        'stats': stats,
        'chart_labels': json.dumps(chart_labels),
        'chart_scores': json.dumps(chart_scores),
    })


@login_required
def start_test(request, subject_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    n = subject.questions_per_test

    # Check if there's already an in-progress attempt
    existing = TestAttempt.objects.filter(
        user=request.user, subject=subject, status='in_progress'
    ).first()
    if existing:
        return redirect('take_test', attempt_id=existing.pk)

    questions = _build_test_questions(subject, n, user=request.user)
    if len(questions) < 1:
        from django.contrib import messages
        messages.error(request, 'No questions available for this subject yet. Check back soon!')
        return redirect('dashboard')

    attempt = TestAttempt.objects.create(
        user=request.user,
        subject=subject,
        total_questions=len(questions),
    )
    for i, q in enumerate(questions, start=1):
        TestQuestion.objects.create(test_attempt=attempt, question=q, order=i)

    return redirect('take_test', attempt_id=attempt.pk)


@login_required
def take_test(request, attempt_id):
    attempt = get_object_or_404(TestAttempt, pk=attempt_id, user=request.user)

    if attempt.status != 'in_progress':
        return redirect('test_results', attempt_id=attempt.pk)

    test_questions = attempt.test_questions.select_related('question').all()
    elapsed = (timezone.now() - attempt.started_at).total_seconds()
    remaining = max(0, attempt.subject.test_duration_minutes * 60 - int(elapsed))

    return render(request, 'practice/take_test.html', {
        'attempt': attempt,
        'test_questions': test_questions,
        'remaining_seconds': remaining,
        'subject': attempt.subject,
    })


@login_required
@require_POST
def save_answer(request, attempt_id):
    """HTMX endpoint: save a single answer and return updated nav pill."""
    attempt = get_object_or_404(TestAttempt, pk=attempt_id, user=request.user)
    if attempt.status != 'in_progress':
        return HttpResponseBadRequest('Test already submitted.')

    try:
        data = json.loads(request.body)
        order = int(data.get('order', 0))
        answer = data.get('answer', '').upper()
        mark_review = data.get('mark_review', None)
    except (json.JSONDecodeError, ValueError):
        return HttpResponseBadRequest('Invalid data.')

    tq = get_object_or_404(TestQuestion, test_attempt=attempt, order=order)
    if answer in ('A', 'B', 'C', 'D'):
        tq.selected_answer = answer
        tq.answered_at = timezone.now()
    if mark_review is not None:
        tq.marked_for_review = bool(mark_review)
    tq.save()

    return JsonResponse({'status': 'ok', 'order': order, 'answer': tq.selected_answer, 'marked': tq.marked_for_review})


@login_required
@require_POST
def submit_test(request, attempt_id):
    attempt = get_object_or_404(TestAttempt, pk=attempt_id, user=request.user)
    if attempt.status != 'in_progress':
        return redirect('test_results', attempt_id=attempt.pk)

    try:
        data = json.loads(request.body)
        timed_out = data.get('timed_out', False)
        elapsed = int(data.get('elapsed_seconds', 0))
        answers = data.get('answers', {})  # {order: letter}
    except (json.JSONDecodeError, ValueError):
        timed_out = False
        elapsed = 0
        answers = {}

    # Apply any last-minute answers
    for order_str, letter in answers.items():
        try:
            tq = attempt.test_questions.get(order=int(order_str))
            if letter.upper() in ('A', 'B', 'C', 'D'):
                tq.selected_answer = letter.upper()
                tq.save()
        except (TestQuestion.DoesNotExist, ValueError):
            pass

    # Evaluate
    correct = 0
    incorrect = 0
    for tq in attempt.test_questions.select_related('question').all():
        if tq.selected_answer:
            tq.is_correct = (tq.selected_answer == tq.question.correct_answer)
            if tq.is_correct:
                correct += 1
            else:
                incorrect += 1
            tq.save()

    total = attempt.total_questions
    accuracy = (correct / total * 100) if total > 0 else 0

    attempt.status = 'timed_out' if timed_out else 'submitted'
    attempt.submitted_at = timezone.now()
    attempt.duration_seconds = elapsed
    attempt.score = correct
    attempt.correct_count = correct
    attempt.incorrect_count = incorrect
    attempt.accuracy = round(accuracy, 1)
    attempt.save()

    return JsonResponse({'status': 'ok', 'redirect': f'/results/{attempt.pk}/'})


@login_required
def test_results(request, attempt_id):
    attempt = get_object_or_404(TestAttempt, pk=attempt_id, user=request.user)
    if attempt.status == 'in_progress':
        return redirect('take_test', attempt_id=attempt.pk)

    test_questions = attempt.test_questions.select_related('question__subject', 'question__topic').all()
    incorrect_tqs = [tq for tq in test_questions if tq.is_correct is False]
    unanswered = [tq for tq in test_questions if tq.selected_answer is None]

    return render(request, 'practice/results.html', {
        'attempt': attempt,
        'test_questions': test_questions,
        'incorrect_tqs': incorrect_tqs,
        'unanswered': unanswered,
        'subject': attempt.subject,
    })


@login_required
def history(request):
    attempts = TestAttempt.objects.filter(
        user=request.user, status__in=['submitted', 'timed_out']
    ).select_related('subject').order_by('-started_at')
    return render(request, 'practice/history.html', {'attempts': attempts})
