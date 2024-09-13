from django.shortcuts import render

# Create your views here.
def sstatic(request):
    return render(request,'sstatic.html')