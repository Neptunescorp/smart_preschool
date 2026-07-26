from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),
    path("", include("authentication.urls")),

    path("students/", include("students.urls")),
    path("teachers/", include("teachers.urls")),
    path("classrooms/", include("classrooms.urls")),
    path("attendance/", include("attendance.urls")),
    path("behavior/", include("behavior.urls")),
    path("parents/", include("parents.urls")),
    path("announcements/", include("announcements.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )