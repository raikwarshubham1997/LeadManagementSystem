from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_teamleader = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)