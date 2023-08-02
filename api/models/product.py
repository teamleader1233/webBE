from django.db import models
from django_bleach.models import BleachField


class Product(models.Model):
    name = BleachField(max_length=64)
    price = models.PositiveBigIntegerField(default=1)
    description = BleachField(max_length=512)

    def __str__(self):
        return self.name