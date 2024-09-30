from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_country(request):
    cid=input('Enter Country id:')
    cname=input('Enter Country Name:')
    CO=Country.objects.get_or_create(Countryid=cid,Countrynm=cname)
    if CO[1]:
        d={'country':Country.objects.all()}
        return render(request,'display_country.html',d)
        #return HttpResponse('Create New Object Successfuly')
    else:
        return HttpResponse('Dear User This Object is already exit')
# def insert_capital(request):
#     cid=input('Enter Country id:')
#     caid=input('Enter Capital id:')
#     caname=input('Capital Name:')
#     CO=Country.objects.get_or_create(Countryid=cid)[0]
#     CAO=Capital.objects.get_or_create(Countryid=CO,Capitalid=caid,Capitalnm=caname)
#     if CAO[1]:
#         return HttpResponse('Create New Object Successfully')
#     else:
#         return HttpResponse('Dear User This Object is already exit')
def insert_capital(request):
    cid=input('Enter Country id:')
    caid=input('Enter Capital id:')
    caname=input('Capital Name:')
    QLCO=Country.objects.filter(Countryid=cid)
    if QLCO:
        CO=QLCO[0]
        CAO=Capital.objects.get_or_create(Countryid=CO,Capitalid=caid,Capitalnm=caname)
        d={'capital':Capital.objects.all()}
        return render(request,'display_capital.html',d)
        #return HttpResponse('New objete Created')
    else:
        return HttpResponse('Dear User This Object is already Exit')
def display_country(request):
    country=Country.objects.all()
    d={'country':country}
    return render(request,'display_country.html',d)
def display_capital(request):
    capital=Capital.objects.all()
    d={'capital':capital}
    return render(request,'display_capital.html',d)