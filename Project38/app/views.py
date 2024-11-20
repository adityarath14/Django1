from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.
def fbv_string(request):
    return HttpResponse('<h1>This FBV string</h1>')
class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1> This Is CbvString</h1>')
def fbv_html(request):
    return render(request,'fbv_html.html')
class CbvHtml(View):
    def get(self,request):
        return render(request,'CbvHtml.html')
def insert_student_fbv(request):
    ESFO=StudentMF()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('DOne')
        else:
            return HttpResponse('Invalid')
    return render(request,'insert_student_fbv.html',d)
class CbvCreateStudent(View):
    def get(self,request):
        ESFO=StudentMF()
        d={'ESFO':ESFO}
        return render(request,'CbvCreateStudent.html',d)
    def post(self,request):
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('DOne')
        else:
            return HttpResponse('Invalid')