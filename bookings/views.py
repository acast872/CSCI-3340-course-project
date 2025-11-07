from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Room, Reservation
from django.utils import timezone

@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'bookings/room_list.html', {'rooms': rooms})


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'bookings/my_reservations.html', {'reservations': reservations})


@login_required
def reserve_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        start = request.POST['start_time']
        end = request.POST['end_time']
        Reservation.objects.create(
            room=room,
            user=request.user,
            start_time=start,
            end_time=end
        )
        return redirect('my_reservations')
    return render(request, 'bookings/reserve_room.html', {'room': room})


@permission_required('bookings.change_reservation')
def approve_reservation(request, res_id):
    res = get_object_or_404(Reservation, id=res_id)
    res.status = 'APPROVED'
    res.save()
    return redirect('admin:index')

