from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages

from .models import Announcement
from .forms import AnnouncementForm


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'
    paginate_by = 20

    def get_queryset(self):
        return Announcement.objects.filter(status=Announcement.STATUS_APPROVED).order_by('-created_at')


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcements/create_announcement.html'
    success_url = reverse_lazy('announcement_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        # status remains PENDING by default
        response = super().form_valid(form)
        messages.success(self.request, "Announcement submitted for moderation.")
        return response


class ModerateAnnouncementsView(PermissionRequiredMixin, ListView):
    permission_required = ('announcements.can_moderate_announcements',)
    template_name = 'announcements/moderate_announcements.html'
    context_object_name = 'pending_announcements'
    paginate_by = 25

    def get_queryset(self):
        return Announcement.objects.filter(status=Announcement.STATUS_PENDING).order_by('created_at')


class ApproveAnnouncementView(PermissionRequiredMixin, View):
    permission_required = ('announcements.can_moderate_announcements',)

    def post(self, request, pk):
        ann = get_object_or_404(Announcement, pk=pk)
        ann.approve()
        messages.success(request, f"Announcement '{ann.title}' approved.")
        return redirect('moderate_announcements')


class RejectAnnouncementView(PermissionRequiredMixin, View):
    permission_required = ('announcements.can_moderate_announcements',)

    def post(self, request, pk):
        ann = get_object_or_404(Announcement, pk=pk)
        ann.reject()
        messages.success(request, f"Announcement '{ann.title}' rejected.")
        return redirect('moderate_announcements')
