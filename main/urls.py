from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('new_meeting/', views.new_meeting, name='new_meeting'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.meeting, name='meeting'),
    path('transcript/', views.transcript, name='transcript'),
    path('meeting/<int:id>', views.meeting, name='meeting'),
    path('calendar', views.calendar, name='calendar'),
] 
