from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=request.POST['tn']
            TO=Topic.objects.get_or_create(topic_name=tn)
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    EWFO=WebPageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebPageForm(request.POST)
        if WFDO.is_valid():
            tn=request.POST['tn']
            nm=request.POST['nm']
            ul=request.POST['ul']
            el=request.POST['el']
            TO=Topic.objects.get(topic_name=tn)
            WO=WebPage.objects.get_or_create(topic_name=TO,name=nm,url=ul,email=el)
            return HttpResponse('WebPage is Created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_webpage.html',d)
def insert_accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            nm=request.POST['nm']
            au=request.POST['au']
            dt=request.POST['dt']
            WO=WebPage.objects.get(id=nm)
            AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=dt)
            return HttpResponse('AccessRecord is Created')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_accessrecord.html',d)