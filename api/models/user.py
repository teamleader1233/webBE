from typing import Any, Iterable, Optional
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
    

class SvnUser(AbstractUser):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True, blank=False)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        self.username = self.get_full_name()
        return super().save(force_insert, force_update, using, update_fields)