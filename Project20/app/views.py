from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    tn=input('Enter Topic Name:')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        return HttpResponse('New object is created')
    else:
        return  HttpResponse('Object is already exist')
def insert_webpage(request):
    tn=input('Enter Topic Name:')
    Name=input('Enter Name:')
    Url=input('Enter url:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=WebPage.objects.get_or_create(topic_name=TO,name=Name,url=Url)
    if WO[1]:
        return HttpResponse('New object is created')
    else:
        return  HttpResponse('Object is already exist')
def insert_accessrecord(request):
    Name=input('Enter Name:')
    Author=input('Enter Author:')
    Date=input('Enter date:')
    WO=WebPage.objects.get_or_create(name=Name)[0]
    AO=AccessRecord.objects.get_or_create(name=WO,author=Author,date=Date)
    if AO[1]:
        return HttpResponse('New object is created')
    else:
        return  HttpResponse('Object is already exist')