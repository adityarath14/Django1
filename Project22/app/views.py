from django.shortcuts import render

# Create your views here.
from app.models import *
def EmpDept(request):
    LEDO=EMP.objects.select_related('DEPTNO').all()
    LEDO=EMP.objects.select_related('DEPTNO').filter(JOB='SALESMAN')
    LEDO=EMP.objects.select_related('DEPTNO').filter(COMM__isnull=False)
    LEDO=EMP.objects.select_related('DEPTNO').filter(MGR__isnull=True)
    LEDO=EMP.objects.select_related('DEPTNO').filter(MGR__isnull=True,ENAME__startswith='K')
    d={'LEDO':LEDO}
    return render(request,'EmpDept.html',d)