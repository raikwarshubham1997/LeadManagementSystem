from django.db import models
from django.contrib.auth.models import User
from SuperAdmin.models import LeadCreate
from datetime import datetime

# Create your models here.
class Manager(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # lead_ass = models.ForeignKey(LeadCreate, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email =  models.EmailField(max_length=200)
    password = models.CharField(max_length=30)
    date_joined = datetime.now()
    