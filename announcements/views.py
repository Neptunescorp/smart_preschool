from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.decorators import teacher_required
from .models import Announcement


# Everyone who is logged in can VIEW announcements
@method_decorator(login_required, name="dispatch")
class AnnouncementListView(ListView):
    model = Announcement
    template_name = "announcements/announcement_list.html"
    context_object_name = "announcements"


# Only teachers/admins can CREATE announcements
@method_decorator(teacher_required, name="dispatch")
class AnnouncementCreateView(CreateView):
    model = Announcement

    fields = [
        "title",
        "message",
        "is_active",
    ]

    template_name = "announcements/announcement_form.html"
    success_url = reverse_lazy("announcement_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# Only teachers/admins can EDIT announcements
@method_decorator(teacher_required, name="dispatch")
class AnnouncementUpdateView(UpdateView):
    model = Announcement

    fields = [
        "title",
        "message",
        "is_active",
    ]

    template_name = "announcements/announcement_form.html"
    success_url = reverse_lazy("announcement_list")


# Only teachers/admins can DELETE announcements
@method_decorator(teacher_required, name="dispatch")
class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = "announcements/announcement_delete.html"
    success_url = reverse_lazy("announcement_list")