from django.contrib.auth.models import User
from django.db import models
from wallet.models import Fitcoin


# Create your models here.
class Product(models.Model):
    fitcoins = models.IntegerField(default=0)

    def price_usd(self):
        # RETRIEVING FROM MONEY OBJECT
        return Fitcoin.to_usd(self.fitcoins)

    def __str__(self):
        return str(self.fitcoins) + " Fitcoins"


class Order(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(default=0)  # Insert product.price_usd()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer.username) + ": " + str(self.product) + " : [PAID: " + str(self.paid) + "]"
