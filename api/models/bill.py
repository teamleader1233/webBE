from typing import Iterable, Optional
from uuid import uuid4

from django.db import models
from django_bleach.models import BleachField


STATUS_CHOICES = (
    ('pending', 'Đang chờ'),
    ('paid', 'Đã thanh toán'),
    ('delivered', 'Đã giao hàng'),
    ('canceled', 'Đã hủy'),
)


class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)
    sender_name = BleachField(max_length=64)
    sender_phone = BleachField(max_length=16)
    sender_address = BleachField(max_length=256)
    receiver_name = BleachField(max_length=64)
    receiver_phone = BleachField(max_length=16)
    receiver_address = BleachField(max_length=256)
    product_image = models.ImageField(blank=True, null=True, default=None)
    product_name = BleachField(max_length=64)
    product_price = models.PositiveBigIntegerField(default=1)
    product_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    product_description = BleachField(max_length=512)
    precollected_price = models.PositiveBigIntegerField(default=1)
    location = BleachField(max_length=256)
    quantity = models.PositiveBigIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(auto_now=True)
    note = BleachField(max_length=512, null=True, default=None)
    total = models.PositiveBigIntegerField()

    class Meta:
        ordering = ['-date']
    
    def save(self, *args, **kwargs) -> None:
        self.total = self.product.price * self.quantity
        return super(Bill, self).save(*args, **kwargs)