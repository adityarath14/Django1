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
def EmpMgr(request):
    LEMO=EMP.objects.select_related('MGR').all()
    LEMO=EMP.objects.select_related('MGR').filter(MGR__isnull=False)
    LEMO=EMP.objects.select_related('MGR').filter(DEPTNO=30)
    LEMO=EMP.objects.select_related('MGR').filter(SAL__gt=3000)
    LEMO=EMP.objects.select_related('MGR').filter(MGR__SAL__gt=3000)
    d={'LEMO':LEMO}
    return render(request,'EmpMgr.html',d)
def EmpDeptMgr(request):
    LEDMO=EMP.objects.select_related('DEPTNO','MGR').all()
    LEDMO=EMP.objects.select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='RESEARCH')
    LEDMO=EMP.objects.select_related('DEPTNO','MGR').filter(MGR__ENAME='SCOTT')
    LEDMO=EMP.objects.select_related('DEPTNO','MGR').filter(COMM__isnull=False)
    d={'LEDMO':LEDMO}
    return render(request,'EmpDeptMgr.html',d)
def DeptEmp(request):
    LEDMO=DEPT.objects.prefetch_related('emp_set').all()
    d={'LEDMO':LEDMO}
    return render(request,'DeptEmp.html',d)