from django import forms
from ..models import FrontendEvent


class FrontendEventForm(forms.ModelForm):
    event_type = forms.CharField(required=True, max_length=30)
    user_id = forms.IntegerField(required=False)
    current_url = forms.CharField(required=True, max_length=256)
    event_meta = forms.CharField(required=True, max_length=1024)
    session_meta = forms.CharField(required=False, max_length=1024)

    class Meta:
        model = FrontendEvent
        exclude = ['event_time']
        fields = ('event_type', 'user_id', 'current_url', 'event_meta', 'session_meta')