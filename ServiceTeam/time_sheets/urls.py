from django.urls import path
from time_sheets import views

app_name = 'time_sheets'

urlpatterns = [
    path('team', views.TeamListView.as_view(), name='teamlist')
]
