from django.db import models

# Create your models here.
class Topic(models.Model):
    def __str__(self):
        return self.topic_name
    topic_name=models.CharField(max_length=20,primary_key=True)
class WebPage(models.Model):
    def __str__(self):
        return self.url
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()
class AccessRecord(models.Model):
    def __str__(self):
        return self.author
    name=models.ForeignKey(WebPage, on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    date=models.DateField()