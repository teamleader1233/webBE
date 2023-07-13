from django.db import models
from django.contrib.auth.models import User, AnonymousUser


class SvnUser(User):
    uuid = models.CharField(primary_key=True, unique=True, blank=False)