from django import forms
from file_upload.models import *

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture']
        widget = {'picture' : forms.FileInput() }