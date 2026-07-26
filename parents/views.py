from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Parent
from attendance.models import Attendance
from behavior.models import Behavior
from announcements.models import Announcement


@login_required
def parent_dashboard(request):

    parent = Parent.objects.get(user=request.user)

    children = parent.children.all()

    attendance = Attendance.objects.filter(
        student__in=children
    ).order_by("-date")

    behaviors = Behavior.objects.filter(
        student__in=children
    ).order_by("-date")

    announcements = Announcement.objects.filter(
        is_active=True
    )[:5]

    return render(
        request,
        "parents/dashboard.html",
        {
            "parent": parent,
            "children": children,
            "attendance": attendance,
            "behaviors": behaviors,
            "announcements": announcements,
        },
    )