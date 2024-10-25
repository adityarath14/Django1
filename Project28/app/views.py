from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def studentdjf(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invalid Data')
    return render(request,'studentdjf.html',d)