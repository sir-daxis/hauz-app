from django.urls import path

from . import views

app_name = 'meetings'
urlpatterns = [
    path('', views.home, name='home'),
    path('meeting_list/', views.MeetingList.as_view(), name='meeting_list'),
    path('live-meeting/<unique_meeting_name>', views.meeting, name='meeting')
]