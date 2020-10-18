from django.utils.translation import gettext_lazy as gt
from django.db import models
import datetime

# This is an ugly hack, I know but the django way has a weird type missmach where you need to submit
# an integer with the form but we want a text to have it more readable. This works if every
# Creating and writing operation is guarded by `X in FRONTEND_EVENT_TYPES`
FRONTEND_EVENT_TYPES = [
    'OTHER',
    'BUTTON_PRESS',
    'JS_ERROR'
    # We could add stuff like DISCONNECT, CONNECT etc but this is enough for now :)
]


# Create your models here.
class FrontendEvent(models.Model):
    event_time = models.DateTimeField(auto_now=True)
    event_type = models.CharField(max_length=30)
    user_id = models.IntegerField(null=True, default=None)
    current_url = models.CharField(max_length=256)
    event_meta = models.CharField(max_length=1024)
    session_meta = models.CharField(null=True, max_length=1024, default=None)

    def __str__(self):
        return str(self.event_type)
