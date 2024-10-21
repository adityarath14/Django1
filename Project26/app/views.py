from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_company(request):
    COMPANYNAME=input('Enter Company Name:')
    CO=Company.objects.get_or_create(company_name=COMPANYNAME)
    if CO[1]:
        companyes=Company.objects.all()
        d={'companyes':companyes}
        return render(request,'display_company.html',d)
    else:
        return HttpResponse('Object already exit')
def insert_model(request):
    pass
def insert_details(request):
    pass
def display_company(request):
    companyes=Company.objects.all()
    d={'companyes':companyes}
    return render(request,'display_company.html',d)