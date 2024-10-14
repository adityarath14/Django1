from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
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
def insert_webpage(request):
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
        return HttpResponse('Dear User This Object is already exit')
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
    #topics=Topic.objects.all()
    #topics=Topic.objects.order_by('topic_name')
    #topics=Topic.objects.order_by('-topic_name')
    #topics=Topic.objects.order_by(Length('topic_name'))
    #topics=Topic.objects.order_by(Length('topic_name').desc())
    #topics=Topic.objects.exclude(topic_name='Ram Laxman')
    topics=Topic.objects.filter(topic_name='My Father')
    d={'topics':topics}
    return render(request,'display_topics.html',d)
def display_webpage(request):
    webpage=WebPage.objects.all()
    #webpage=WebPage.objects.order_by('name')
    #webpage=WebPage.objects.order_by('-name')
    #webpage=WebPage.objects.order_by(Length('name'))
    #webpage=WebPage.objects.order_by(Length('name').desc())
    #webpage=WebPage.objects.exclude(name='Aditya Rath')
    #webpage=WebPage.objects.filter(name='Raju')
    #webpage=WebPage.objects.filter(name__startswith='A')
    #webpage=WebPage.objects.filter(name__endswith='u')
    #webpage=WebPage.objects.filter(topic_name__in=('My Mother','Real Hero','My Father'))
    #webpage=WebPage.objects.filter(name__contains='u')
    #webpage=WebPage.objects.filter(name__regex=r'A')
    d={'webpage':webpage}
    return render(request,'display_webpage.html',d)
def display_accessrecord(request):
    accessrecord=AccessRecord.objects.all()
    #accessrecord=AccessRecord.objects.order_by('author')
    #accessrecord=AccessRecord.objects.order_by('-author')
    #accessrecord=AccessRecord.objects.order_by(Length('author'))
    #accessrecord=AccessRecord.objects.order_by(Length('author').desc())
    #accessrecord=AccessRecord.objects.exclude(author='Raju')
    #accessrecord=AccessRecord.objects.filter(author='Aditya')
    # accessrecord=AccessRecord.objects.filter(date__gt='2000-09-14')
    # accessrecord=AccessRecord.objects.filter(date__gte='2000-09-14')
    # accessrecord=AccessRecord.objects.filter(date__lt='2000-09-14')
    # accessrecord=AccessRecord.objects.filter(date__lte='2000-09-14')
    # accessrecord=AccessRecord.objects.filter(date__month='04')
    # accessrecord=AccessRecord.objects.filter(date__year='2020')
    # accessrecord=AccessRecord.objects.filter(date__day='14')
    d={'accessrecord':accessrecord}
    return render(request,'display_accessrecord.html',d)
def update_webpage(request):
    webpage=WebPage.objects.filter(name='Jay').update(url='http://www.realhero.com')
    webpage=WebPage.objects.filter(name='Raju').update(email='rintu@gmail.com')
    webpage=WebPage.objects.filter(email='rintu@gmail.com').update(name='Rajkishor')
    webpage=WebPage.objects.update_or_create(name='Akash',defaults={'url':'http://www.mymother.com'})
    TO=Topic.objects.get(topic_name='My Mother')
    WebPage.objects.update_or_create(name='Aditya Rath',defaults={'topic_name':TO})
    WebPage.objects.update_or_create(name='Adi',defaults={'topic_name':TO})
    WebPage.objects.update_or_create(name='Adi',defaults={'url':'http://www.drJ.com'})
    webpage=WebPage.objects.all()
    d={'webpage':webpage}
    return render(request,'display_webpage.html',d)