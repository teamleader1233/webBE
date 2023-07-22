from django.db import models
from django_bleach.models import BleachField


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = BleachField(max_length=512)
    image = models.ImageField(upload_to='products', blank=True)

    def __str__(self):
        return self.name