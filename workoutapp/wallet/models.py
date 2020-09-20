from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fitcoin = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + ": " + str(self.fitcoin)

    def add_balance(self, fitcoins: float):
        self.fitcoin += fitcoins
        self.save()


class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sender.username + "-->" + self.receiver.username + " : " + str(self.amount)
