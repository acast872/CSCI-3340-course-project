from django import forms
from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your announcement...', 'class': 'form-control', 'rows': 6}),
        }
