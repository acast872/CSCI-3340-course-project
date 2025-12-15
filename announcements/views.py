from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Announcement

def announcement_list(request):
    announcements = Announcement.objects.filter(status='APPROVED').order_by('-created_at')
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})


@login_required
def create_announcement(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Announcement.objects.create(title=title, content=content, author=request.user)
        return redirect('announcement_list')
    return render(request, 'announcements/create_announcement.html')


@permission_required('announcements.change_announcement')
def moderate_announcements(request):
    pending = Announcement.objects.filter(status='PENDING')
    return render(request, 'announcements/moderate_announcements.html', {'pending': pending})


@permission_required('announcements.change_announcement')
def approve_announcement(request, ann_id):
    ann = get_object_or_404(Announcement, id=ann_id)
    ann.status = 'APPROVED'
    ann.save()
    return redirect('moderate_announcements')


@permission_required('announcements.change_announcement')
def reject_announcement(request, ann_id):
    ann = get_object_or_404(Announcement, id=ann_id)
    ann.status = 'REJECTED'
    ann.save()
    return redirect('moderate_announcements')
