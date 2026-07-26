from django.urls import path
from .views import (
    ClassroomListView,
    ClassroomCreateView,
    ClassroomUpdateView,
    ClassroomDeleteView,
    ClassroomDetailView,
)

urlpatterns = [
    path("", ClassroomListView.as_view(), name="classroom_list"),
    path("add/", ClassroomCreateView.as_view(), name="classroom_add"),
    path("<int:pk>/", ClassroomDetailView.as_view(), name="classroom_detail"),
    path("<int:pk>/edit/", ClassroomUpdateView.as_view(), name="classroom_edit"),
    path("<int:pk>/delete/", ClassroomDeleteView.as_view(), name="classroom_delete"),
]