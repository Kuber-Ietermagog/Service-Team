from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('newuser', views.newuser, name='newuser'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('user_update/<int:pk>', views.UserUpdateView.as_view(), name='user_update'),
    path('profile_update/<int:pk>', views.UserProfileInfoUpdateView.as_view(), name='profile_update'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
]
