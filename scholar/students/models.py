
from django.db import models

class User(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=500)
    nombre=models.CharField(max_length=500,default='')