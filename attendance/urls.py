from django.urls import path
from . import views

urlpatterns = [
    path("", views.AttendanceListView.as_view(), name="attendance_list"),

    path(
        "take/",
        views.take_attendance,
        name="take_attendance",
    ),

    path(
        "<int:pk>/delete/",
        views.AttendanceDeleteView.as_view(),
        name="attendance_delete",
    ),
]