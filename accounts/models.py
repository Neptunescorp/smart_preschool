from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    PARENT = "PARENT"

    ROLE_CHOICES = [
        (ADMIN, "Administrator"),
        (TEACHER, "Teacher"),
        (PARENT, "Parent"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=PARENT,
    )

    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"