from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default='📚')
    test_duration_minutes = models.PositiveIntegerField(default=25)
    questions_per_test = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ['subject', 'name']

    def __str__(self):
        return f"{self.subject.name} — {self.name}"


class Question(models.Model):
    DIFFICULTY_EASY = 'easy'
    DIFFICULTY_MEDIUM = 'medium'
    DIFFICULTY_HARD = 'hard'
    DIFFICULTY_CHOICES = [
        (DIFFICULTY_EASY, 'Easy'),
        (DIFFICULTY_MEDIUM, 'Medium'),
        (DIFFICULTY_HARD, 'Hard'),
    ]

    ANSWER_CHOICES = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default=DIFFICULTY_MEDIUM)
    text = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)
    explanation = models.TextField(help_text='Step-by-step explanation of the correct answer')
    source = models.CharField(max_length=200, blank=True, default='Custom')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.subject.name}][{self.difficulty}] {self.text[:60]}"

    def get_option(self, letter):
        return {
            'A': self.option_a,
            'B': self.option_b,
            'C': self.option_c,
            'D': self.option_d,
        }.get(letter.upper(), '')

    def options_list(self):
        return [
            ('A', self.option_a),
            ('B', self.option_b),
            ('C', self.option_c),
            ('D', self.option_d),
        ]


class TestAttempt(models.Model):
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_SUBMITTED = 'submitted'
    STATUS_TIMED_OUT = 'timed_out'
    STATUS_CHOICES = [
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_SUBMITTED, 'Submitted'),
        (STATUS_TIMED_OUT, 'Timed Out'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_attempts')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, through='TestQuestion')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_IN_PROGRESS)
    started_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    total_questions = models.PositiveIntegerField(default=20)
    correct_count = models.PositiveIntegerField(null=True, blank=True)
    incorrect_count = models.PositiveIntegerField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-started_at']

    def __str__(self):
        return f"{self.user.username} — {self.subject.name} — {self.started_at:%Y-%m-%d %H:%M}"

    def formatted_duration(self):
        if self.duration_seconds is None:
            return '—'
        m, s = divmod(self.duration_seconds, 60)
        return f"{m}m {s}s"


class TestQuestion(models.Model):
    """Ordered questions in a test attempt, with user's answer."""
    test_attempt = models.ForeignKey(TestAttempt, on_delete=models.CASCADE, related_name='test_questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    selected_answer = models.CharField(max_length=1, blank=True, null=True)
    is_correct = models.BooleanField(null=True, blank=True)
    marked_for_review = models.BooleanField(default=False)
    answered_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['order']
        unique_together = ['test_attempt', 'order']

    def __str__(self):
        return f"Q{self.order} of attempt {self.test_attempt_id}"
