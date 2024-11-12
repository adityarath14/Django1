from django.shortcuts import render
from app.forms import *
# Create your views here.
def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO, 'EPFO':EPFO}
    return render(request,'registration.html',d)
