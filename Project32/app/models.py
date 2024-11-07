from django.db import models
from django.core.validators import *
# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=100,validators=[MinLengthValidator(5)])
    sid=models.IntegerField()
    semail=models.EmailField()