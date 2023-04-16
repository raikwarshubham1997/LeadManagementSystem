from django.db import models
from django.contrib.auth.models import User
from datetime import *






class LeadCreate(models.Model):

    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    birthday =  models.DateField(max_length=150)
    email = models.EmailField(max_length=150)
    contact = models.CharField(max_length=12)
    alternat_no = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    permanent_address = models.CharField(max_length=500)
    intrested =  models.CharField(max_length=150)
    lead_sources = models.CharField(max_length=150)
    remarks =  models.TextField(max_length=500)
    assigned =  models.CharField(max_length=200)
    status =  models.CharField(max_length=150)
    date_create = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name


class Call_Details(models.Model):
    cls = models.CharField(max_length=50)
    rem = models.CharField(max_length=250)
    str_dt = models.CharField(max_length=50)
    end_dt = models.DateTimeField(auto_now_add=True)
    led_id = models.ForeignKey(LeadCreate, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cls

class Notes_Details(models.Model):
    msg = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    led_id = models.ForeignKey(LeadCreate, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.msg