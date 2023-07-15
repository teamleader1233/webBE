from typing import Iterable, Optional
from django.db import models

from uuid import uuid4

from ..models.product import Product


STATUS_CHOICES = (
    ('pending', 'Đang chờ'),
    ('paid', 'Đã thanh toán'),
    ('delivered', 'Đã giao hàng'),
    ('canceled', 'Đã hủy'),
)

PAYMENT_CHOICES = (
    ('cod', 'Thanh toán khi nhận hàng'),
    ('momo', 'Thanh toán qua MoMo'),
    ('zalopay', 'Thanh toán qua ZaloPay'),
    ('bank', 'Thanh toán qua ngân hàng'),
)


class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey(Product, to_field='id', on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=3, default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    address = models.CharField(max_length=80)
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cod')
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        return self.quantity * self.product.price
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        old_date = self.updated_at
        bill : Bill = super().save(force_insert, force_update, using, update_fields)
        BillHistory.objects.create(
            bill=bill,
            updated_at=old_date
        )
    

class BillHistory(models.Model):
    bill = models.ForeignKey(Bill, to_field='id', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-updated_at']