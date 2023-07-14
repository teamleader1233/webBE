from typing import Any, Optional
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User, UserManager


class SvnUserManager(UserManager):
    def create_user(self, 
                    first_name: str, 
                    last_name: str,
                    email: str, 
                    password: str | None = ..., **extra_fields: Any) -> Any:
        uid = uuid4()
        username: str = "%s %s" % (first_name, last_name).strip()
        user: SvnUser = self.create(
            uid=uid,
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user
    

class SvnUser(User):
    uid = models.CharField(max_length=36, unique=True, primary_key=True, db_index=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    USERNAME_FIELD = 'email'

    objects = SvnUserManager