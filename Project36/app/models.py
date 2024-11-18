from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=20)
    sdevice=models.CharField(max_length=20)