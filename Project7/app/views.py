from django.shortcuts import render

# Create your views here.
def TitleBody(request):
    return render(request,'Title&Body.html')