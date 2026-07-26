from django.urls import path

from .views import (
    TeacherListView,
    TeacherDetailView,
    TeacherCreateView,
    TeacherUpdateView,
    TeacherDeleteView,
)

urlpatterns = [
    path("", TeacherListView.as_view(), name="teacher_list"),
    path("add/", TeacherCreateView.as_view(), name="teacher_add"),
    path("<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
    path("<int:pk>/edit/", TeacherUpdateView.as_view(), name="teacher_edit"),
    path("<int:pk>/delete/", TeacherDeleteView.as_view(), name="teacher_delete"),
]