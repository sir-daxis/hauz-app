from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from django.utils.text import slugify
from datetime import timedelta


# Create your models here.
DEFAULT_HOST_ID = 1
class Meeting(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    host = models.ForeignKey(User, related_name='host', on_delete=models.CASCADE, default=DEFAULT_HOST_ID)
    title_of_meeting = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    starting_date_time = models.DateTimeField()
    ending_date_time = models.DateTimeField()
    unique_meeting_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.creator}: {self.title_of_meeting}'

    def save(self, *args, **kwargs):
        if self.duration:
            self.ending_date_time = self.starting_date_time + timedelta(minutes=self.duration)
        elif not self.ending_date_time:
            self.ending_date_time = self.starting_date_time + timedelta(hours=1)

        if not self.unique_meeting_name:
            self.unique_meeting_name = slugify(str(self.title_of_meeting)
                                               + '-'
                                               + str(uuid.uuid4()))

        if not self.host:
            self.host = 1

        return super(Meeting, self).save()

    @property
    def meeting_time(self):
        return (timezone.now() >= self.starting_date_time)

    @property
    def after_meeting(self):
        return (timezone.now() >= self.ending_date_time)


