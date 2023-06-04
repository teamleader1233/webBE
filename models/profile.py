from django.db import models
from django.contrib.auth.models import User

class Customer(User):
    is_superuser = False
    is_staff = False

class Admin(User):
    is_staff = True
    is_superuser = False