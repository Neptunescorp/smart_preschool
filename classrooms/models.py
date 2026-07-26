from django.db import models
from teachers.models import Teacher


class Classroom(models.Model):
    name = models.CharField(max_length=100)

    age_group = models.CharField(max_length=50)

    capacity = models.PositiveIntegerField(default=20)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="classrooms",
    )

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name