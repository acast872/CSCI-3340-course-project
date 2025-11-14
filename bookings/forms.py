from django import forms
from .models import Reservation, Room

class MeetupForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class MeetupInfoForm(forms.Form):
    name = forms.CharField(max_length=100, label="Meetup Name")
    description = forms.CharField(widget=forms.Textarea, label="Description")