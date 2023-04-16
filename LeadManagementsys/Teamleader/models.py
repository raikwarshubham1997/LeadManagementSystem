from django.db import models
from StaffManager.models import Employee_Register
from django.contrib.auth.models import User


# Create your models here.
class Worker_Register(models.Model):
    created_by = models.ForeignKey(Employee_Register, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    email =  models.EmailField(max_length=200)
    password = models.CharField(max_length=30)