from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from workout.models import Exercise


class Messages(models.Model):
    Sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Sender')
    Receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Receiver')
    Messages = models.CharField(max_length=250, default="")
    SendDate = models.DateTimeField(auto_now=True)
    Seen = models.BooleanField(default="")


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    firstName = models.CharField(max_length=20, default="")
    lastName = models.CharField(max_length=20, default="")
    age = models.IntegerField(default=20)
    image = models.CharField(
        max_length=250,
        default="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png")
    CreatedAt = models.DateTimeField(auto_now=True)
    friends = models.ManyToManyField("UserInfo", blank=True)
    
    def __str__(self):
        return str(self.user.username)

    def get_abs_url(self):
        return "/accounts/profile/{}".format(self.slug)



class Follow(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Username')
    Following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Following')
    FollowedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Username.username


class FriendRequest(models.Model):
    FromUser = models.ForeignKey(User, related_name='FromUser', on_delete=models.CASCADE)
    ToUser = models.ForeignKey(User, related_name='ToUser', on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(auto_now=True)