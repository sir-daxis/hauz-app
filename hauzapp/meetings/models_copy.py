from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.timezone import now
from django.utils.text import slugify
import datetime


# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Meeting(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title_of_meeting = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    starting_date_time = models.DateTimeField()
    ending_date_time = models.DateTimeField()
    unique_meeting_name = models.TextField(blank=True, null=True)

    # project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.creator}: {self.title_of_meeting}'

    # def save(self, *args, **kwargs):
    #     if not self.unique_meeting_name:
    #         self.unique_meeting_name = slugify(
    #             str(self.title_of_meeting) + '-' + str(uuid.uuid4())
    #         )
    #     return super(Meeting, self).save()

    @property
    def meeting_time(self):
        return (datetime.datetime.now() >= self.starting_date_time) and (
                datetime.datetime.now() <= self.date.ending_date_time)
