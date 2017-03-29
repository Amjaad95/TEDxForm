from django import forms
from django.utils import timezone
from core.models import Regestiration

class RegestirationForm(forms.ModelForm):
    class Meta:
        model = Regestiration
        exclude = ['submission', 'modification']
