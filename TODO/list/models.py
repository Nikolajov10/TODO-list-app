from datetime import datetime
from django.db import models

# Create your models here.
class Task(models.Model):
    username = models.CharField(max_length=40)
    description = models.TextField(max_length=20000)
    due_date = models.DateField()
    priority = models.CharField(max_length=10)
    title  = models.CharField(max_length=50,default="Task")

    def setDiff(self,date_difference):
        self.diff = date_difference