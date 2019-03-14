from django import forms
from .models import Image, Profile
from django.contrib.auth.models import User

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('pic', 'description')


class ProfileEditForm(forms.ModelForm):

   class Meta:
      model = Profile
      fields = ['pic','bio']




