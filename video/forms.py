from django import forms
from .models import VideoContent

class VideoCreateForm(forms.ModelForm):
    class Meta:
        model = VideoContent
        fields = "__all__"