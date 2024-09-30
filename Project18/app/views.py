from django.shortcuts import render

# Create your views here.
def Parent(request):
    return render(request,'Parent.html')
def Child(request):
    return render(request,'Child.html')