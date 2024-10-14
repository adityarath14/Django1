from django.db import models

# Create your models here.
class Catagory(models.Model):
    PCID=models.IntegerField(primary_key=True)
    PCTYPE=models.CharField(max_length=20)
    def __str__(self):
        return self.PCTYPE
class Products(models.Model):
    PID=models.IntegerField(primary_key=True)
    PNAME=models.CharField(max_length=14)
    PRICE=models.IntegerField(max_length=8)
    MDATE=models.DateField()
    MPLACE=models.CharField(max_length=15)
    PCID=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.PNAME