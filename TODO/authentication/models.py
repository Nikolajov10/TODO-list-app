from django.db import models

# Create your models here.
class RegUsers(models.Model):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)