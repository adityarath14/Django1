from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Rohit(request):
    return HttpResponse('<h1>Rohit Played Pull short Very Well</h1>')
def Hardhik(request):
    return render(request,'Hardhik.html')