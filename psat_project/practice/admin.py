from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import Subject, Topic, Question, TestAttempt, TestQuestion


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'questions_per_test', 'test_duration_minutes']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    list_filter = ['subject']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['short_text', 'subject', 'topic', 'difficulty', 'correct_answer', 'active', 'source']
    list_filter = ['subject', 'topic', 'difficulty', 'active']
    search_fields = ['text', 'explanation']
    list_editable = ['active', 'difficulty']
    actions = ['export_csv']

    def short_text(self, obj):
        return obj.text[:80]
    short_text.short_description = 'Question'

    def export_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="questions.csv"'
        writer = csv.writer(response)
        writer.writerow(['subject', 'topic', 'difficulty', 'text', 'option_a', 'option_b',
                         'option_c', 'option_d', 'correct_answer', 'explanation', 'source'])
        for q in queryset:
            writer.writerow([
                q.subject.name, q.topic.name if q.topic else '', q.difficulty,
                q.text, q.option_a, q.option_b, q.option_c, q.option_d,
                q.correct_answer, q.explanation, q.source,
            ])
        return response
    export_csv.short_description = 'Export selected questions to CSV'


class TestQuestionInline(admin.TabularInline):
    model = TestQuestion
    extra = 0
    readonly_fields = ['question', 'order', 'selected_answer', 'is_correct', 'marked_for_review']
    can_delete = False


@admin.register(TestAttempt)
class TestAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'status', 'score', 'total_questions',
                    'correct_count', 'accuracy_pct', 'started_at', 'formatted_duration']
    list_filter = ['subject', 'status']
    search_fields = ['user__username']
    readonly_fields = ['user', 'subject', 'status', 'started_at', 'submitted_at',
                       'duration_seconds', 'score', 'correct_count', 'incorrect_count', 'accuracy']
    inlines = [TestQuestionInline]

    def accuracy_pct(self, obj):
        if obj.accuracy is not None:
            return f"{obj.accuracy:.1f}%"
        return '—'
    accuracy_pct.short_description = 'Accuracy'

    def formatted_duration(self, obj):
        return obj.formatted_duration()
    formatted_duration.short_description = 'Duration'
