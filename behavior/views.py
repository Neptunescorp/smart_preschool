from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator

from accounts.decorators import teacher_required

from students.models import Student
from .models import Behavior
from .ai import generate_progress_report
from .ai_service import generate_ai_analysis


@teacher_required
def behavior_report(request, pk):

    behavior = get_object_or_404(
        Behavior,
        pk=pk,
    )

    if not behavior.ai_report:
        behavior.ai_report = generate_progress_report(behavior)
        behavior.save(update_fields=["ai_report"])

    return render(
        request,
        "behavior/report.html",
        {
            "behavior": behavior,
        },
    )


@teacher_required
def behavior_analysis(request, student_id):

    student = get_object_or_404(
        Student,
        pk=student_id,
    )

    behaviors = Behavior.objects.filter(
        student=student
    ).order_by("date")

    report = generate_ai_analysis(student)

    return render(
        request,
        "behavior/behavior_analysis.html",
        {
            "student": student,
            "behaviors": behaviors,
            "report": report,
        },
    )


@method_decorator(teacher_required, name="dispatch")
class BehaviorListView(ListView):
    model = Behavior
    template_name = "behavior/behavior_list.html"
    context_object_name = "behaviors"


@method_decorator(teacher_required, name="dispatch")
class BehaviorCreateView(CreateView):
    model = Behavior
    fields = "__all__"
    template_name = "behavior/behavior_form.html"
    success_url = reverse_lazy("behavior_list")


@method_decorator(teacher_required, name="dispatch")
class BehaviorUpdateView(UpdateView):
    model = Behavior
    fields = "__all__"
    template_name = "behavior/behavior_form.html"
    success_url = reverse_lazy("behavior_list")


@method_decorator(teacher_required, name="dispatch")
class BehaviorDeleteView(DeleteView):
    model = Behavior
    template_name = "behavior/behavior_delete.html"
    success_url = reverse_lazy("behavior_list")