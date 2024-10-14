from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def insert_catagory(request):
    PCID=int(input('Enter ProductCatagory ID:'))
    PCTYPE=input('Enter Produ Type:')
    CO=Catagory.objects.get_or_create(PCID=PCID)
    if CO[1]:
        catagory=Catagory.objects.all()
        d={'catagory':catagory}
        return render(request,'insert_catagory.html',d)
    else:
        return HttpResponse('Dear User This object is Already Exit')
def insert_products(request):
    PID=int(input('Enter Product ID:'))
    PNAME=input('Enter Product Name:')
    PRICE=input('Enter Product Price:')
    MDATE=input('Enter Manufacturing Date:')
    MPLACE=input('Enter Manufacturing Place:')
    PCID=input('Enter ProductCatagory ID')
    