from django.db import models
from django.db.models import (
    CharField,
    DateField,
    TimeField,
    DecimalField,
    ForeignKey,
    CASCADE
)
from .utils import sum_points


class Receipt(models.Model):
    retailer = CharField(max_length=250)
    purchaseDate = DateField()
    purchaseTime = TimeField()
    
    @property
    def total(self):
        total = 0
        for item in self.item_set.all():
            total += item.price

        return total

    def points(self):
        return sum_points(self, self.item_set.all())


class Item(models.Model):
    shortDescription = CharField(max_length=250)
    price = DecimalField(max_digits=100, decimal_places=2)
    receipt = ForeignKey(Receipt, on_delete=CASCADE)
