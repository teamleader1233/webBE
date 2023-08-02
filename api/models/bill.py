from typing import Iterable, Optional
from uuid import uuid4

from django.db import models
from django_bleach.models import BleachField

from ..models.product import Product


STATUS_CHOICES = (
    ('pending', 'Đang chờ'),
    ('paid', 'Đã thanh toán'),
    ('delivered', 'Đã giao hàng'),
    ('canceled', 'Đã hủy'),
)


class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    location = BleachField(max_length=255, default='Chưa xác định')
    date = models.DateTimeField(auto_now=True)
    total = models.PositiveBigIntegerField()
    
    def save(self, *args, **kwargs) -> None:
        self.total = self.product.price * self.quantity
        return super(Bill, self).save(*args, **kwargs)