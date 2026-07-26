from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.decorators import teacher_required

from .models import Attendance
from students.models import Student
from classrooms.models import Classroom


@method_decorator(teacher_required, name="dispatch")
class AttendanceListView(ListView):
    model = Attendance
    template_name = "attendance/attendance_list.html"
    context_object_name = "attendance"


@method_decorator(teacher_required, name="dispatch")
class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = "attendance/attendance_delete.html"
    success_url = reverse_lazy("attendance_list")


@teacher_required
def take_attendance(request):

    classrooms = Classroom.objects.all()

    classroom_id = request.GET.get("classroom")
    students = Student.objects.none()

    if classroom_id:
        students = Student.objects.filter(classroom_id=classroom_id)

    if request.method == "POST":

        classroom_id = request.POST.get("classroom")

        date = request.POST.get("date")

        if not date:
            date = timezone.now().date()

        classroom = Classroom.objects.get(id=classroom_id)
        teacher = classroom.teacher

        for student in Student.objects.filter(classroom_id=classroom_id):

            status = request.POST.get(f"student_{student.id}")

            Attendance.objects.update_or_create(
                student=student,
                date=date,
                defaults={
                    "teacher": teacher,
                    "status": status,
                },
            )

        return redirect("attendance_list")

    return render(
        request,
        "attendance/take_attendance.html",
        {
            "classrooms": classrooms,
            "students": students,
            "today": timezone.now().date(),
        },
    )