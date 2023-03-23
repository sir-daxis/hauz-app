from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.urls import reverse
from django.utils import timezone
import datetime

from .forms import MeetingCreateForm
from .models import Meeting


# Create your views here.
def home(request):
    form = MeetingCreateForm()
    if request.method == 'POST':
        form = MeetingCreateForm(request.POST)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.creator = request.user
            fm.save()

            return HttpResponseRedirect(reverse('meetings:meeting_list'))

    return render(request, 'meetings/home.html', {'form': form})


class MeetingList(generic.ListView):
    model = Meeting
    template_name = 'meetings/meeting_list.html'
    context_object_name = 'meetings'

    def get_queryset(self):
        return Meeting.objects.filter(creator=self.request.user).order_by('-starting_date_time')


def meeting(request, unique_meeting_name):
    message = None
    meeting = get_object_or_404(Meeting, unique_meeting_name=unique_meeting_name)

    if not meeting.meeting_time:
        now = timezone.localtime()
        t = abs(now - meeting.starting_date_time).total_seconds()
        hours_get, minutes_get, seconds_get = seconds_to_time(t)

        message = (f'It is not the time for meeting {meeting.title_of_meeting}. Meeting starts in '
                   f'{hours_get}:{minutes_get}:{seconds_get}.')
        messages.warning(request, message)

        return HttpResponseRedirect(reverse('meetings:home'))

    elif meeting.after_meeting:
        now = timezone.localtime()
        t = abs(meeting.starting_date_time - now).total_seconds()
        hours_get, minutes_get, seconds_get = seconds_to_time(t)

        message = (f'The meeting {meeting.title_of_meeting} ended '
                   f'{hours_get}:{minutes_get}:{seconds_get} ago.')
        messages.warning(request, message)

        return HttpResponseRedirect(reverse('meetings:home'))

    if request.user == meeting.creator:
        """render the view for meeting host"""
        return render(request, 'meetings/host_page.html', {'meeting': meeting})

    return render(request, 'meetings/meeting_page.html', {'meeting': meeting})


def seconds_to_time(t):
    minutes_get, seconds_get = divmod(t, 60)
    hours_get, minutes_get = divmod(minutes_get, 60)
    return hours_get, minutes_get, seconds_get

