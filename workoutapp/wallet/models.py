from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fitcoin = models.FloatField(default=0)


class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    amount = models.FloatField(default=0)
    date = models.DateTimeField(auto_now=True)


class Purchase(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField(default=0)
    date = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)









