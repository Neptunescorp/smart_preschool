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

from .models import Classroom


@method_decorator(teacher_required, name="dispatch")
class ClassroomListView(ListView):
    model = Classroom
    template_name = "classrooms/classroom_list.html"
    context_object_name = "classrooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_classrooms"] = Classroom.objects.count()
        context["active_classrooms"] = Classroom.objects.filter(
            is_active=True
        ).count()
        return context


@method_decorator(teacher_required, name="dispatch")
class ClassroomDetailView(DetailView):
    model = Classroom
    template_name = "classrooms/classroom_detail.html"


@method_decorator(teacher_required, name="dispatch")
class ClassroomCreateView(CreateView):
    model = Classroom
    fields = "__all__"
    template_name = "classrooms/classroom_form.html"
    success_url = reverse_lazy("classroom_list")


@method_decorator(teacher_required, name="dispatch")
class ClassroomUpdateView(UpdateView):
    model = Classroom
    fields = "__all__"
    template_name = "classrooms/classroom_form.html"
    success_url = reverse_lazy("classroom_list")


@method_decorator(teacher_required, name="dispatch")
class ClassroomDeleteView(DeleteView):
    model = Classroom
    template_name = "classrooms/classroom_delete.html"
    success_url = reverse_lazy("classroom_list")