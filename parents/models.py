from django.db import models
from django.conf import settings


class Parent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="parent_profile",
    )
    phone = models.CharField(max_length=20)

    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username