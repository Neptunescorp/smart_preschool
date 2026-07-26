from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.utils.decorators import method_decorator
from django.contrib import messages

from accounts.decorators import teacher_required
from accounts.models import User

from .models import Teacher


@method_decorator(teacher_required, name="dispatch")
class TeacherListView(ListView):
    model = Teacher
    template_name = "teachers/teacher_list.html"
    context_object_name = "teachers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_teachers"] = Teacher.objects.count()
        context["active_teachers"] = Teacher.objects.filter(
            is_active=True
        ).count()
        return context


@method_decorator(teacher_required, name="dispatch")
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "teachers/teacher_detail.html"


@method_decorator(teacher_required, name="dispatch")
class TeacherCreateView(CreateView):
    model = Teacher

    fields = [
        "first_name",
        "last_name",
        "gender",
        "email",
        "phone",
        "address",
        "qualification",
        "experience",
        "salary",
        "photo",
        "joining_date",
        "is_active",
    ]

    template_name = "teachers/teacher_form.html"
    success_url = reverse_lazy("teacher_list")

    def form_valid(self, form):

        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]

        # Generate username
        username = (
            first_name.lower() +
            last_name.lower()
        )

        # Make username unique
        counter = 1

        while User.objects.filter(username=username).exists():
            username = f"{first_name.lower()}{last_name.lower()}{counter}"
            counter += 1

        # Default password
        password = "Teacher123"

        # Create login account
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=User.TEACHER,
        )

        # Link Teacher -> User
        form.instance.user = user

        messages.success(
            self.request,
            f"""
Teacher account created!

Username: {username}
Password: {password}
            """,
        )

        return super().form_valid(form)


@method_decorator(teacher_required, name="dispatch")
class TeacherUpdateView(UpdateView):
    model = Teacher

    fields = [
        "first_name",
        "last_name",
        "gender",
        "email",
        "phone",
        "address",
        "qualification",
        "experience",
        "salary",
        "photo",
        "joining_date",
        "is_active",
    ]

    template_name = "teachers/teacher_form.html"
    success_url = reverse_lazy("teacher_list")


@method_decorator(teacher_required, name="dispatch")
class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = "teachers/teacher_delete.html"
    success_url = reverse_lazy("teacher_list")