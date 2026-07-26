from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.utils.decorators import method_decorator

from accounts.decorators import teacher_required

from .models import Student


@method_decorator(teacher_required, name="dispatch")
class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_students"] = Student.objects.count()
        context["active_students"] = Student.objects.filter(
            is_active=True
        ).count()

        return context


@method_decorator(teacher_required, name="dispatch")
class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_detail.html"


@method_decorator(teacher_required, name="dispatch")
class StudentCreateView(CreateView):
    model = Student

    fields = [
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "parent_name",
        "parent_phone",
        "address",
        "classroom",
        "photo",
        "is_active",
    ]

    template_name = "students/student_form.html"
    success_url = reverse_lazy("student_list")


@method_decorator(teacher_required, name="dispatch")
class StudentUpdateView(UpdateView):
    model = Student

    fields = [
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "parent_name",
        "parent_phone",
        "address",
        "photo",
        "is_active",
    ]

    template_name = "students/student_form.html"
    success_url = reverse_lazy("student_list")


@method_decorator(teacher_required, name="dispatch")
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_delete.html"
    success_url = reverse_lazy("student_list")