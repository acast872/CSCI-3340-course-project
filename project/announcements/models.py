from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL  # string; use get_user_model() in runtime if needed


class Announcement(models.Model):
    STATUS_PENDING = 'PENDING'
    STATUS_APPROVED = 'APPROVED'
    STATUS_REJECTED = 'REJECTED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending Approval'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcements')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        permissions = [
            ('can_moderate_announcements', 'Can moderate announcements'),
        ]

    def __str__(self):
        return f"{self.title} ({self.status})"

    def approve(self):
        self.status = self.STATUS_APPROVED
        self.updated_at = timezone.now()
        self.save(update_fields=['status', 'updated_at'])

    def reject(self):
        self.status = self.STATUS_REJECTED
        self.updated_at = timezone.now()
        self.save(update_fields=['status', 'updated_at'])
