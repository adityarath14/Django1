from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insertTopic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse(f'{tn}Topic is Created')
    return render(request,'insertTopic.html')
def insertWebPage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        nm=request.POST['nm']
        ul=request.POST['ul']
        el=request.POST['el']
        TO=Topic.objects.get(topic_name=tn)
        WO=WebPage.objects.get_or_create(topic_name=TO,name=nm,url=ul,email=el)
        return HttpResponse('Webpage is Created')
    return render(request,'insertWebPage.html',d)
def insertAccessRecord(request):
    LWO=WebPage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        nm=request.POST['nm']
        ar=request.POST['ar']
        dt=request.POST['dt']
        WO=WebPage.objects.get(id=nm)
        AO=AccessRecord.objects.get_or_create(name=WO,author=ar,date=dt)
        return HttpResponse('AccessRecord is Created')
    return render(request,'insertAccessRecord.html',d)
def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MTN=request.POST.getlist('tn')
        EQST=WebPage.objects.none()
        for topic in MTN:
            EQST=EQST|WebPage.objects.filter(topic_name=topic)
        d1={'EQST':EQST}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)
def select_accessrecord(request):
    LWO=WebPage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        MWN=request.POST.getlist('nm')
        EQST=AccessRecord.objects.none()
        for webpage in MWN:
            EQST=EQST|AccessRecord.objects.filter(name=webpage)
        d1={'EQST':EQST}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'select_accessrecord.html',d)
def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)
def checkbox_accessrecord(request):
    LWO=WebPage.objects.all()
    d={'LWO':LWO}
    return render(request,'checkbox_accessrecord.html',d)