from django import forms
from django.contrib.auth.models import User
from . import models


class ClockForm(forms.ModelForm):
    class Meta:
        model = models.ClockEntry
        fields = '__all__'
