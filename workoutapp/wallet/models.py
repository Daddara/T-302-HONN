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


class Fitcoin:
    TRANSLATION_CURRENCY = "USD"
    EXCHANGE_RATE = 50

    @classmethod
    def to_usd(cls, fitcoins: int) -> float:
        return round(fitcoins/cls.EXCHANGE_RATE, 2)

    @classmethod
    def to_fitcoin(cls, usd: float) -> int:
        return round(cls.EXCHANGE_RATE*usd)

    @classmethod
    def translation_currency(cls) -> str:
        return cls.TRANSLATION_CURRENCY















