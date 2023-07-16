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


class AbstractBill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bill(AbstractBill):
    product = models.ForeignKey(Product, to_field='id', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100)
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cod')
    total = models.IntegerField()
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        self.total = self.product.price * self.quantity
        bill : Bill = super(Bill, self).save(force_insert, force_update, using, update_fields)
        BillHistory.objects.create(
            id=id,
            status=bill.status,
            date_created=bill.date_created
        )
    

class BillHistory(models.Model):
    bill = models.ForeignKey(Bill, to_field='id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']