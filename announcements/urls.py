from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcement_list, name='announcement_list'),
    path('new/', views.create_announcement, name='create_announcement'),
    path('moderate/', views.moderate_announcements, name='moderate_announcements'),
    path('approve/<int:ann_id>/', views.approve_announcement, name='approve_announcement'),
    path('reject/<int:ann_id>/', views.reject_announcement, name='reject_announcement'),
]
