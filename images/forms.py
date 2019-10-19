from django import forms
from django.utils import timezone

from .models import Post


class UploadImageForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=False, initial='MyImage')
    private = forms.BooleanField(required=False)
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = ('title', 'image', 'private')


