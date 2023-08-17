from typing import Iterable, Optional
from uuid import uuid4
from secrets import token_urlsafe

from django.db import models
from django_bleach.models import BleachField


STATUS_CHOICES = (
    ('pending', 'Đang chờ'),
    ('paid', 'Đã thanh toán'),
    ('delivered', 'Đã giao hàng'),
    ('canceled', 'Đã hủy'),
)

DELIVERY_CHOICES = (
    ('nd', 'Nội địa'),
    ('vt', 'Việt-Trung'),
)


def bill_token():
    return token_urlsafe(7)


class Bill(models.Model):
    id = models.CharField(primary_key=True, default=bill_token, editable=False, max_length=10)
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
    product_description = BleachField(max_length=512, default='')
    precollected_price = models.PositiveBigIntegerField(default=1)
    delivery_option = models.CharField(max_length=2, choices=DELIVERY_CHOICES, null=True, default=None)
    delivery_address = BleachField(max_length=256)
    current_location = BleachField(max_length=256, default='')
    quantity = models.PositiveBigIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(auto_now=True)
    note = BleachField(max_length=512, default='')
    total_price = models.PositiveBigIntegerField(default=1)

    class Meta:
        ordering = ['-date']
    
    def save(self, *args, **kwargs) -> None:
        self.delivery_option = 'nd'
        if self.delivery_address.split('/')[-1] == 'Trung Quốc':
            self.delivery_option == 'vt'
        return super(Bill, self).save(*args, **kwargs)