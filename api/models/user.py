from typing import Any, Optional
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User, UserManager
    

class SvnUser(User):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    USERNAME_FIELD = 'email'