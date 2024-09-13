from django.shortcuts import render

# Create your views here.
def Conditions(request):
    d={'a':10,'b':20}
    return render(request,'Conditions.html',context=d)