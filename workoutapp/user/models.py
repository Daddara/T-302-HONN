from django.contrib.auth.models import User
from django.db import models


class Messages(models.Model):
    Sender = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='Sender')
    Receiver = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='Receiver')
    Messages = models.CharField(max_length=250, blank=True)
    SenderDate = models.DateField(blank=True)
    Seen = models.BooleanField(blank=True)

class UserInfo(models.Model):
    User = models.ForeignKey(User,  on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=250, blank=True)
    LastName = models.CharField(max_length=250, blank=True)
    BirthYear = models.DateField(blank=True)
    Image = models.CharField(max_length=250, blank=True)
    CreatedAt = models.DateField(blank=True)
