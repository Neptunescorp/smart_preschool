from django.db import models
from django.conf import settings


class Teacher(models.Model):

    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
        null=True,
        blank=True,
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=10,
        choices=GENDER,
    )

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    address = models.TextField()

    qualification = models.CharField(max_length=200)

    experience = models.PositiveIntegerField(
        help_text="Years of experience"
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    photo = models.ImageField(
        upload_to="teachers/",
        blank=True,
        null=True,
    )

    joining_date = models.DateField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"