from django.shortcuts import render
from django.utils import timezone

from students.models import Student
from teachers.models import Teacher
from classrooms.models import Classroom
from attendance.models import Attendance
from behavior.models import Behavior


def dashboard(request):

    today = timezone.now().date()

    total_students = Student.objects.count()

    present = Attendance.objects.filter(
        date=today,
        status="Present"
    ).count()

    absent = Attendance.objects.filter(
        date=today,
        status="Absent"
    ).count()

    late = Attendance.objects.filter(
        date=today,
        status="Late"
    ).count()

    behaviors = Behavior.objects.all()

    if behaviors.exists():

        avg_communication = round(
            sum(b.communication for b in behaviors) / behaviors.count(), 2
        )

        avg_confidence = round(
            sum(b.confidence for b in behaviors) / behaviors.count(), 2
        )

        avg_creativity = round(
            sum(b.creativity for b in behaviors) / behaviors.count(), 2
        )

        avg_teamwork = round(
            sum(b.teamwork for b in behaviors) / behaviors.count(), 2
        )

    else:

        avg_communication = 0
        avg_confidence = 0
        avg_creativity = 0
        avg_teamwork = 0

    context = {

        "students": total_students,
        "teachers": Teacher.objects.count(),
        "classrooms": Classroom.objects.count(),
        "behaviors": behaviors.count(),

        "present_today": present,
        "absent_today": absent,

        "recent_students": Student.objects.order_by("-id")[:5],
        "recent_behaviors": behaviors.order_by("-date")[:5],

        "attendance_chart": [
            present,
            absent,
            late,
        ],

        "behavior_chart": [
            avg_communication,
            avg_confidence,
            avg_creativity,
            avg_teamwork,
        ],
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )