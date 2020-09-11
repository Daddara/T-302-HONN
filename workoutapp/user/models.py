from django.contrib.auth.models import User
from django.db import models
import datetime


class Messages(models.Model):
    Sender = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='Sender')
    Receiver = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='Receiver')
    Messages = models.CharField(max_length=250, default="")
    SendDate = models.DateTimeField(auto_now=True)
    Seen = models.BooleanField(default="")

class UserInfo(models.Model):
    User = models.ForeignKey(User,  on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=20, default="")
    LastName = models.CharField(max_length=20, default="")
    BirthYear = models.DateTimeField(default=datetime.date.today())
    Image = models.CharField(
        max_length=250,
        default="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png")
    CreatedAt = models.DateTimeField(auto_now=True)
