from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def MSD(request):
    return HttpResponse('<h1>Captain Cool Of India</h1>')
def Raina(request):
    return render(request,'Raina.html')