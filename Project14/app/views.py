from django.shortcuts import render

# Create your views here.
def sfiles(request):
    return render(request,'sfiles.html')