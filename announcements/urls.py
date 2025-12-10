from django.urls import path
from .views import (
    AnnouncementListView, AnnouncementCreateView,
    ModerateAnnouncementsView, ApproveAnnouncementView, RejectAnnouncementView
)

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement_list'),
    path('new/', AnnouncementCreateView.as_view(), name='create_announcement'),
    path('moderate/', ModerateAnnouncementsView.as_view(), name='moderate_announcements'),
    # Use POST for modify actions; views expect POST at these endpoints.
    path('approve/<int:pk>/', ApproveAnnouncementView.as_view(), name='approve_announcement'),
    path('reject/<int:pk>/', RejectAnnouncementView.as_view(), name='reject_announcement'),
]
