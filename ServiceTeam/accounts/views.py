from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate,login,logout
from accounts.forms import UserForm, UserProfileInfoForm
from . import forms
from . import models


def newuser(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/newuser.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



## Users View
class UserListView(ListView):
    context_object_name = 'club_users'
    model = models.UserProfileInfo

class UserUpdateView(UpdateView):
    fields = ('username', 'first_name', 'last_name', 'email')
    model = models.User
    success_url = reverse_lazy('accounts:user_list')

class UserProfileInfoUpdateView(UpdateView):
    fields = ('profile_pic', 'cell_phone')
    model = models.UserProfileInfo
    success_url = reverse_lazy('accounts:user_list')

def password_change_done(request):
    return render(request, 'accounts/password_change_done.html')
