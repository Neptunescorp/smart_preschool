from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.BehaviorListView.as_view(),
        name="behavior_list",
    ),

    path(
        "add/",
        views.BehaviorCreateView.as_view(),
        name="behavior_add",
    ),

    path(
        "<int:pk>/edit/",
        views.BehaviorUpdateView.as_view(),
        name="behavior_edit",
    ),

    path(
        "<int:pk>/delete/",
        views.BehaviorDeleteView.as_view(),
        name="behavior_delete",
    ),
    path(
        "<int:pk>/report/",
        views.behavior_report,
        name="behavior_report",
    ),
    path(
    "analysis/<int:student_id>/",
    views.behavior_analysis,
    name="behavior_analysis",
),

]