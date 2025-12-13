from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_meetup, name='create_meetup'),
    path('<int:room_id>/reserve/', views.reserve_room, name='reserve_room'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('approve/<int:res_id>/', views.approve_reservation, name='approve_reservation'),
    path('join/', views.join_meetups, name='join_meetups'),
    path('join/<int:meetup_id>/', views.join_meetup, name='join_meetup'),


]
