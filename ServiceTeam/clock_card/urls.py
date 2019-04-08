from django.urls import path
from clock_card import views

app_name = 'clock_card'

urlpatterns = [
    path('clock', views.ClockView.as_view(), name='clock')
]
