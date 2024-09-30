from django.db import models

# Create your models here.
class Country(models.Model):
    def __str__(self):
        return self.Countryid
    def __str__(self):
        return self.Countrynm
    Countryid=models.IntegerField(max_length=10,primary_key=True)
    Countrynm=models.CharField(max_length=50)
class Capital(models.Model):
    def __str__(self):
        return self.Capitalid
    def __str__(self):
        return self.Capitalnm
    Countryid=models.ForeignKey(Country,on_delete=models.CASCADE)
    Capitalid=models.IntegerField(max_length=10)
    Capitalnm=models.CharField(max_length=50)