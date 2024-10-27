from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def insert_school(request):
    sname=input('Enter School Name:')
    SO=School.objects.get_or_create(school_name=sname)
    if SO[1]:
        return HttpResponse('New Object Created Successfully')
    else:
        return HttpResponse('This Object is already exit')
def insert_student(request):
    sname=input('Enter School Name:')
    stuid=input('Enter Student Id:')
    stuname=input('Enter Student Name:')
    stustd=input('Enter Student Standard:')
    SO=School.objects.get(school_name=sname)
    STUO=Student.objects.get_or_create(school_name=SO,stu_id=stuid,stu_name=stuname,stu_std=stustd)
    if STUO[1]:
        return HttpResponse('New Object Created Successfully')
    else:
        return HttpResponse('his Object is already exit')
def insert_schoolform(request):
    LSO=School.objects.all()
    d={'LSO':LSO}
    if request.method=='POST':
        sn=request.POST['sn']
        # SO=School.objects.get_or_create(school_name=sn)
        # return HttpResponse(f'{sn} is Created')
    return render(request,'insert_schoolform.html',d)
def insert_studentform(request):
    LSTO=Student.objects.all()
    d={'LSTO':LSTO}
    if request.method=='POST':
        sname=request.POST['sname']
        stuid=request.POST['stuid']
        stuname=request.POST['stuname']
        stustd=request.POST['stustd']
        # SO=School.objects.get(school_name=sname)
        # STUO=Student.objects.get_or_create(school_name=SO,stu_id=stuid,stu_name=stuname,stu_std=stustd)
    return render(request,'insert_studentform.html',d)
def update_student(request):
    student=Student.objects.filter(stu_id=102).update(stu_std='III')
    student=Student.objects.filter(stu_id=105).update(stu_std='IV')
    student=Student.objects.all()
    d={'student':student}
    return render(request,'display_student.html',d)
def delete_student(request):
    student=Student.objects.filter(stu_name='ADITYA').delete()
    student=Student.objects.all()
    d={'student':student}
    return render(request,'display_student.html',d)
def display_school(request):
    school=School.objects.all()
    d={'school':school}
    return render(request,'display_school.html',d)
def display_student(request):
    student=Student.objects.all()
    d={'student':student}
    return render(request,'display_student.html',d)