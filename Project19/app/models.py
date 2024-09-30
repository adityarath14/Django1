from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True)
class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()
class accessmethods(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    date=models.DateField()