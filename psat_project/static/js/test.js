/**
 * Main test controller: handles navigation, answer selection,
 * mark-for-review, HTMX answer saves, and final submission.
 */

// State
const answers = {};       // { order: letter }
const marked = {};        // { order: true/false }
let currentQ = 1;
let totalQ = 0;
let attemptId = null;
let timer = null;
const CSRF_TOKEN = document.querySelector('meta[name="csrf-token"]')?.content || '';

function init(opts) {
  totalQ = opts.totalQ;
  attemptId = opts.attemptId;
  window._testDuration = opts.durationSeconds;

  // Restore any pre-saved answers from server-rendered data
  if (opts.savedAnswers) {
    Object.assign(answers, opts.savedAnswers);
  }
  if (opts.savedMarked) {
    Object.assign(marked, opts.savedMarked);
  }

  renderNav();
  showQuestion(currentQ);

  // Start timer
  timer = new CountdownTimer(opts.remainingSeconds, () => {
    submitTest(true);
  });
  timer.start();
}

// ---------------------------------------------------------------------------
// Navigation
// ---------------------------------------------------------------------------

function showQuestion(order) {
  document.querySelectorAll('.question-card').forEach(el => {
    el.classList.toggle('hidden', parseInt(el.dataset.order) !== order);
  });
  currentQ = order;
  renderNav();
  updateProgress();
}

function prevQ() { if (currentQ > 1) showQuestion(currentQ - 1); }
function nextQ() { if (currentQ < totalQ) showQuestion(currentQ + 1); }

function renderNav() {
  const nav = document.getElementById('question-nav');
  if (!nav) return;
  nav.innerHTML = '';
  for (let i = 1; i <= totalQ; i++) {
    const btn = document.createElement('button');
    btn.textContent = i;
    btn.className = 'nav-pill';
    if (i === currentQ) btn.classList.add('active');
    if (answers[i]) btn.classList.add('answered');
    if (marked[i]) btn.classList.add('flagged');
    btn.onclick = () => showQuestion(i);
    nav.appendChild(btn);
  }
}

function updateProgress() {
  const answeredCount = Object.keys(answers).length;
  const pct = totalQ > 0 ? Math.round(answeredCount / totalQ * 100) : 0;
  const bar = document.getElementById('progress-bar');
  const label = document.getElementById('progress-label');
  if (bar) bar.style.width = pct + '%';
  if (label) label.textContent = `${answeredCount} / ${totalQ} answered`;
}

// ---------------------------------------------------------------------------
// Answering
// ---------------------------------------------------------------------------

function selectAnswer(order, letter) {
  answers[order] = letter;
  // Highlight selected option
  document.querySelectorAll(`[data-order="${order}"] .option-btn`).forEach(btn => {
    btn.classList.toggle('selected', btn.dataset.letter === letter);
  });
  renderNav();
  updateProgress();
  // Persist to server
  saveAnswer(order, letter);
}

function toggleReview(order) {
  marked[order] = !marked[order];
  const btn = document.getElementById(`review-btn-${order}`);
  if (btn) {
    btn.textContent = marked[order] ? '🚩 Marked for Review' : '⚑ Mark for Review';
    btn.classList.toggle('marked', marked[order]);
  }
  renderNav();
  saveAnswer(order, null, marked[order]);
}

function saveAnswer(order, letter, markReview) {
  const payload = { order };
  if (letter !== null) payload.answer = letter;
  if (markReview !== undefined) payload.mark_review = markReview;

  fetch(`/test/${attemptId}/save/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN,
    },
    body: JSON.stringify(payload),
  }).catch(() => {});  // silently ignore network errors — answers are in memory
}

// ---------------------------------------------------------------------------
// Submission
// ---------------------------------------------------------------------------

function confirmSubmit() {
  const unanswered = totalQ - Object.keys(answers).length;
  let msg = 'Are you sure you want to submit the test?';
  if (unanswered > 0) {
    msg = `You have ${unanswered} unanswered question(s). Are you sure you want to submit?`;
  }
  if (confirm(msg)) {
    submitTest(false);
  }
}

function submitTest(timedOut) {
  if (timer) timer.pause();
  const elapsed = timer ? timer.elapsed() : 0;

  // Disable submit button to prevent double submit
  const btn = document.getElementById('submit-btn');
  if (btn) { btn.disabled = true; btn.textContent = 'Submitting...'; }

  fetch(`/test/${attemptId}/submit/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN,
    },
    body: JSON.stringify({ timed_out: timedOut, elapsed_seconds: elapsed, answers }),
  })
    .then(r => r.json())
    .then(data => {
      if (data.redirect) window.location.href = data.redirect;
    })
    .catch(() => {
      // Fallback: redirect to dashboard
      window.location.href = '/dashboard/';
    });
}

// ---------------------------------------------------------------------------
// Modals
// ---------------------------------------------------------------------------

function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) {
    modal.classList.remove('hidden');
    if (id === 'whiteboard-modal') Whiteboard.init();
  }
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('hidden');
}

// Close modal on backdrop click
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-backdrop')) {
    e.target.classList.add('hidden');
  }
});
