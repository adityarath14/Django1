from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO, 'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST, request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('Registration','Registration Successfully','rathaditya14@gmail.com',[MUFDO.email],fail_silently=False)
            return HttpResponse('Registeration is Successfully')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'registration.html',d)
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Not an Active User')
        return HttpResponse('Invalid Credentials')
    return render(request,'user_login.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
@login_required
def profile_display(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO, 'PO':PO}
    return render(request,'profile_display.html',d)
@login_required
def change_password(request):
    if request.method=='POST':
        cpw=request.POST['cpw']
        username=request.session['username']
        UO=User.objects.get(username=username)
        UO.set_password(cpw)
        UO.save()
        return HttpResponse('Password is Changed')
    return render(request,'change_password.html')
def reset_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.POST['un']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(pw)
            UO.save()
            return HttpResponse('Password is Changed')
        else:
            return HttpResponse('User is not present')
    return render(request,'reset_password.html')     