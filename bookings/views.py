from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Room, Reservation
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from .forms import MeetupForm, MeetupInfoForm


@login_required
def create_meetup(request):
    if request.method == 'POST':
        info_form = MeetupInfoForm(request.POST)
        meetup_form = MeetupForm(request.POST)
        if info_form.is_valid() and meetup_form.is_valid():
            reservation = meetup_form.save(commit=False)
            reservation.user = request.user
            reservation.status = 'PENDING'  
            reservation.created_at = timezone.now()
            reservation.save()
            return redirect('home')
    else:
        info_form = MeetupInfoForm()
        meetup_form = MeetupForm()
    
    return render(request, 'bookings/create_meetup.html', {
        'info_form': info_form,
        'meetup_form': meetup_form
    })

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'bookings/my_reservations.html', {'reservations': reservations})

def join_meetups(request):
    approved_meetups = Reservation.objects.filter(status='APPROVED')
    return render(request, 'bookings/join_meetups.html', {
        'meetups': approved_meetups
    })

@login_required
def reserve_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        start = request.POST['start_time']
        end = request.POST['end_time']

        conflict = Reservation.objects.filter(
            room=room,
            status__in=['PENDING', 'APPROVED'],
            start_time__lt=end,
            end_time__gt=start
        ).exists()

        if conflict:
            messages.error(request, "This room is already reserved during that time.")
            return redirect('room_list')

        Reservation.objects.create(
            room=room,
            user=request.user,
            start_time=start,
            end_time=end
        )

        messages.success(request, "Room reserved successfully!")
        return redirect('my_reservations')

    return render(request, 'bookings/reserve_room.html', {'room': room})

@permission_required('bookings.change_reservation')
def approve_reservation(request, res_id):
    res = get_object_or_404(Reservation, id=res_id)
    res.status = 'APPROVED'
    res.save()
    return redirect('admin:index')

@login_required
def join_meetup(request, meetup_id):
    try:
        meetup = Reservation.objects.get(id=meetup_id, status='APPROVED')
    except Reservation.DoesNotExist:
        return HttpResponseNotFound("Meetup not found or not approved.")

    meetup.participants.add(request.user)
    meetup.save()

    messages.success(request, f"You have joined the meetup '{meetup.name}'!")
    return redirect('join_meetups')