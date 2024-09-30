from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>Virat Kohali Is The Best Batter In India</h1>')