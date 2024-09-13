from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Virat(request):
    return HttpResponse('<h1>Virat is The King Of Cricket</h1>')
def ABD(request):
    return render(request,'ABD.html')