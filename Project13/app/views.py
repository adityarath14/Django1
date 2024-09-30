from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'Aditya','MOB':[8280952019,6371720557]}
    return render(request,'loop.html',context=d)
def Navigation(request):
    d={'a':100}
    return render(request,'Navigation.html',context=d)