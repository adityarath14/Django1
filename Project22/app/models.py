from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO=models.IntegerField(max_length=2,primary_key=True)
    DNAME=models.CharField(max_length=14)
    LOC=models.CharField(max_length=13)
    #def __str__(self):
    #    return self.DEPTNO
    def __str__(self):
        return str(self.DEPTNO)
    '''def __str__(self):
        return self.LOC'''
class EMP(models.Model):
    EMPNO=models.IntegerField(max_length=4,primary_key=True)
    ENAME=models.CharField(max_length=10)
    JOB=models.CharField(max_length=9)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    HIREDATE=models.DateField()
    SAL=models.FloatField(max_length=7)
    COMM=models.FloatField(max_length=7,null=True,blank=True)
    DEPTNO=models.ForeignKey(DEPT,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.EMPNO)
    def __str__(self):
        return self.ENAME
    # def __str__(self):
    #     return str(self.MGR)
    # def __str__(self):
    #     return self.MGR
    # def __str__(self):
    #     return self.HIREDATE
    # def __str__(self):
    #     return self.SAL
    # def __str__(self):
    #     return self.COMM
class BONUS(models.Model):
    ENAME=models.CharField(max_length=10)
    JOB=models.CharField(max_length=9)
    SAL=models.IntegerField(max_length=4)
    COMM=models.IntegerField(max_length=4)
    def __str__(self):
        return self.ENAME
    def __str__(self):
        return self.JOB
    def __str__(self):
        return self.SAL
    def __str__(self):
        return self.COMM
class SALGRADE(models.Model):
    GRADE=models.IntegerField()
    LOSAL=models.IntegerField()
    HISAL=models.IntegerField()
    def __str__(self):
        return str(self.GRADE)
    # def __str__(self):
    #     return self.LOSAL
    # def __str__(self):
    #     return self.HISAL