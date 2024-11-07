from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_student(request):
    ESMFO=StudentMF()
    d={'ESMFO':ESMFO}
    if request.method=='POST':
        SMFDO=StudentMF(request.POST)
        if SMFDO.is_valid():
            SMFDO.save()
            return HttpResponse('Data is Created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_student.html',d)