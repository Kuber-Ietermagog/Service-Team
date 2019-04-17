from django.urls import path
from clock_card import views

app_name = 'clock_card'

urlpatterns = [
    path('clock', views.MyClockCardList.as_view(), name='clock'),
    path('clock_entry', views.ClockEventCreateView.as_view(), name='clock_entry')
]
