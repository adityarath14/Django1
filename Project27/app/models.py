from django.db import models

# Create your models here.
class School(models.Model):
    school_name=models.CharField(max_length=50,primary_key=True)
    def __str__(self):
        return self.school_name
class Student(models.Model):
    school_name=models.ForeignKey(School,on_delete=models.CASCADE)
    stu_id=models.IntegerField()
    stu_name=models.CharField(max_length=10)
    stu_std=models.CharField(max_length=4)
    def __str__(self):
        return self.stu_name