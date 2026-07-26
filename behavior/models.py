from django.db import models
from students.models import Student
from teachers.models import Teacher

from .ai import generate_progress_report


class Behavior(models.Model):

    RATING = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="behaviors",
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
    )

    date = models.DateField(auto_now_add=True)

    communication = models.IntegerField(choices=RATING)
    confidence = models.IntegerField(choices=RATING)
    creativity = models.IntegerField(choices=RATING)
    teamwork = models.IntegerField(choices=RATING)
    leadership = models.IntegerField(choices=RATING)
    emotional_control = models.IntegerField(choices=RATING)
    problem_solving = models.IntegerField(choices=RATING)

    teacher_notes = models.TextField(
        blank=True,
        verbose_name="Teacher Notes"
    )

    ai_report = models.TextField(
        blank=True,
        editable=False,
        verbose_name="AI Progress Report"
    )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        report = generate_progress_report(self)

        if self.ai_report != report:
            self.ai_report = report
            super().save(update_fields=["ai_report"])

    def __str__(self):
        return f"{self.student} - {self.date}"