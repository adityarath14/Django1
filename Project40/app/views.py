from django.shortcuts import render
from django.views.generic import ListView
from app.models import *
# Create your views here.
class SchoolList(ListView):
    model=School
    #queryset=School.objects.all()
    context_object_name='schools'
    #template_name='app/school_list.html'
    ordering=['scname']