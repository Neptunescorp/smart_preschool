from django.db import models
from students.models import Student
from teachers.models import Teacher


class Attendance(models.Model):

    STATUS = [
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Late", "Late"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance",
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Present",
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-date"]

        unique_together = (
            "student",
            "date",
        )

    def __str__(self):
        return f"{self.student} - {self.date}"