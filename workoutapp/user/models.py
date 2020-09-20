from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Messages(models.Model):
    Sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Sender')
    Receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Receiver')
    Messages = models.CharField(max_length=250, default="")
    SendDate = models.DateTimeField(auto_now=True)
    Seen = models.BooleanField(default="")


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20, default="")
    lastName = models.CharField(max_length=20, default="")
    age = models.IntegerField(default=20)
    image = models.CharField(
        max_length=250,
        default="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png")
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username+"'s info"
