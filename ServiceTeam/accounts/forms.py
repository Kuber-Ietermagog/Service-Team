from django import forms
from accounts.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic', 'employee_no', 'cell_phone', 'job_title', 'department')
