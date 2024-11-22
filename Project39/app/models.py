from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)