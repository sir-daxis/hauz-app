from django import forms
from .models import Meeting


class MeetingCreateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ["title_of_meeting",
                  "starting_date_time"
                  ]

        widgets = {
            "title_of_meeting": forms.TextInput(attrs={"class": "form-control", "placeholder":
                "Title of the Meeting..."}),
            "starting_date_time": forms.DateTimeInput(attrs={"class": "form-control date"})
        }
