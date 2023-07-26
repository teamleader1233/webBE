from django.db import models
from django_bleach.models import BleachField


class Blog(models.Model):
    title = BleachField(max_length=32)
    content = BleachField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)