from django.contrib import admin
from .models import Room, Reservation

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')  # removed 'location' because Room has no 'location' field

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'host', 'start_time', 'end_time', 'status')  # updated fields
    list_filter = ('status', 'start_time')
    actions = ['approve_reservations']

    def approve_reservations(self, request, queryset):
        queryset.update(status='APPROVED')
    approve_reservations.short_description = "Mark selected reservations as approved"