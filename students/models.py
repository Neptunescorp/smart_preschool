from django.db import models
from classrooms.models import Classroom
from parents.models import Parent

class Student(models.Model):
    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=10, choices=GENDER)

    date_of_birth = models.DateField()

    admission_date = models.DateField(auto_now_add=True)

    parent_name = models.CharField(max_length=200)

    parent_phone = models.CharField(max_length=20)

    address = models.TextField()

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students",
    )

    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(default=True)
    
    parent = models.ForeignKey(
    Parent,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="children",
)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"