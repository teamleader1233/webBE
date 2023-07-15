from django.db import models


class Product(models.Model):
    id = models.CharField(max_length=64, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products', blank=True)

    def __str__(self):
        return self.name