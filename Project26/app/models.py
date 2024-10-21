from django.db import models

# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=10,primary_key=True)
    def __str__(self):
        return self.company_name
class Model(models.Model):
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE)
    model_name=models.CharField(max_length=10)
    processor=models.CharField(max_length=10)
    def __str__(self):
        return self.model_name
class Details(models.Model):
    model_name=models.ForeignKey(Model,on_delete=models.CASCADE)
    price=models.IntegerField(max_length=10)
    launch_date=models.DateField()
    def __str__(self):
        return self.price 