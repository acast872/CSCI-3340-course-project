from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/reserve/', views.reserve_room, name='reserve_room'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('approve/<int:res_id>/', views.approve_reservation, name='approve_reservation'),
]
