from django.db import models
from django.contrib.auth.models import User


class Customer(User):
    uuid = models.CharField(primary_key=True, unique=True, blank=False)
    is_verified = False


class Admin(User):
    is_staff = True


class Staff(Admin):
    is_superuser = True