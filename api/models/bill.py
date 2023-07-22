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
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    address = BleachField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    total = models.PositiveBigIntegerField()
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        self.total = self.product.price * self.quantity
        return super(Bill, self).save(force_insert, force_update, using, update_fields)