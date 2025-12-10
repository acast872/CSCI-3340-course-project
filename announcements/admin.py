from django.contrib import admin
from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    actions = ['approve_selected', 'reject_selected']

    def approve_selected(self, request, queryset):
        updated = queryset.update(status=Announcement.STATUS_APPROVED)
        self.message_user(request, f"{updated} announcement(s) approved.")
    approve_selected.short_description = "Approve selected announcements"

    def reject_selected(self, request, queryset):
        updated = queryset.update(status=Announcement.STATUS_REJECTED)
        self.message_user(request, f"{updated} announcement(s) rejected.")
    reject_selected.short_description = "Reject selected announcements"
