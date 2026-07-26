from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "parent_name",
        "parent_phone",
        "is_active",
    )

    search_fields = (
        "first_name",
        "last_name",
        "parent_name",
    )

    list_filter = (
        "gender",
        "is_active",
    )