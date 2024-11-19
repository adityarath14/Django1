from django.db import models

# Create your models here.
class Boy(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    village=models.CharField(max_length=25)