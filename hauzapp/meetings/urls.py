from django.urls import path

from . import views

app_name = 'meetings'
urlpatterns = [
    path('new-meeting', views.create_meeting, name='new_meeting'),
    path('meeting-list/', views.MeetingList.as_view(), name='meeting_list'),
    path('meeting-list-message/<str:message>', views.meeting_list, name='meeting_list_message'),
    path('live-meeting/<unique_meeting_name>', views.meeting, name='meeting'),
]