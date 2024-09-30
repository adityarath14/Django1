from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    TOPICNAME=input('Enter Topic Name:')
    TO=Topic.objects.get_or_create(topic_name=TOPICNAME)
    if TO[1]:
        topics=Topic.objects.all()
        d={'topics':topics}
        return render(request,'display_topics.html',d)
        #return HttpResponse('New object created Successfully')
    else:
        return HttpResponse('Dear User This Object is already exit')
'''def insert_webpage(request):
    TOPICNAME=input('Enter Topic Name:')
    NAME=input('Enter Name:')
    URL=input('Enter url:')
    EMAIL=input('Enter Email Address:')
    TO=Topic.objects.get_or_create(topic_name=TOPICNAME)[0]
    WO=WebPage.objects.get_or_create(topic_name=TO,name=NAME,url=URL,email=EMAIL)
    if WO[1]:
        return HttpResponse('New object created Successfully')
    else:
        return HttpResponse('Dear User This Object is already exit')
def insert_accessrecord(request):
    NAME=input('Enter Name:')
    AUTHOR=input('Enter Author:')
    DATE=input('Enter Date:')
    WO=WebPage.objects.get_or_create(name=NAME)[0]
    AO=AccessRecord.objects.get_or_create(name=WO,author=AUTHOR,date=DATE)
    if AO[1]:
        return HttpResponse('New object created Successfully')
    else:
        return HttpResponse('Dear User This Object is already exit')'''
# def insert_webpage(request):
#     TOPICNAME=input('Enter Topic Name:')
#     NAME=input('Enter Name:')
#     URL=input('Enter url:')
#     EMAIL=input('Enter Email Address:')
#     TO=Topic.objects.get(topic_name=TOPICNAME)
#     WO=WebPage.objects.get_or_create(topic_name=TO,name=NAME,url=URL,email=EMAIL)
#     if WO:
#         return HttpResponse('New Object Created')
# def insert_accessrecord(request):
#     NAME=input('Enter Name:')
#     AUTHOR=input('Enter Author:')
#     DATE=input('Enter Date:')
#     WO=WebPage.objects.get(name=NAME)
#     AO=AccessRecord.objects.get_or_create(name=WO,author=AUTHOR,date=DATE)
#     if AO:
#         return HttpResponse('New Object Created')
def insert_webpage(request):
    TOPICNAME=input('Enter Topic Name:')
    NAME=input('Enter Name:')
    URL=input('Enter url:')
    EMAIL=input('Enter Email Address:')
    QLTO=Topic.objects.filter(topic_name=TOPICNAME)
    if QLTO:
        TO=QLTO[0]
        WO=WebPage.objects.get_or_create(topic_name=TO,name=NAME,url=URL,email=EMAIL)
        d={'webpage':WebPage.objects.all()}
        return render(request,'display_webpage.html',d)
        #return HttpResponse('New object created successfully')
    else:
        return HttpResponse('Dear User This Object is already exit')
def insert_accessrecord(request):
    NAME=input('Enter Name:')
    AUTHOR=input('Enter Author:')
    DATE=input('Enter Date:')
    QLWO=WebPage.objects.filter(name=NAME)
    if QLWO:
        WO=QLWO[0]
        AO=AccessRecord.objects.get_or_create(name=WO,author=AUTHOR,date=DATE)
        d={'accessrecord':AccessRecord.objects.all()}
        return render(request,'display_accessrecord.html',d)
        #return HttpResponse('New object created successfully')
    else:
        return HttpResponse('Dear User This Object is already exit')
def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)
def display_webpage(request):
    webpage=WebPage.objects.all()
    d={'webpage':webpage}
    return render(request,'display_webpage.html',d)
def display_accessrecord(request):
    accessrecord=AccessRecord.objects.all()
    d={'accessrecord':accessrecord}
    return render(request,'display_accessrecord.html',d)