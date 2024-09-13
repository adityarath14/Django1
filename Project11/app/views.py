from django.shortcuts import render

# Create your views here.
def PositiveNegative(request):
    d={'a':10}
    return render(request,'PositiveNegative.html',context=d)