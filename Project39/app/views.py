from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import TemplateView,FormView
# Create your views here.
class RenderHtml(TemplateView):
    template_name='RenderHtml.html'
    def get_context_data(self, **kwargs):
        ECDO= super().get_context_data(**kwargs)
        ECDO['name']='Aditya'
        ECDO['age']=24
        ECDO['ESFO']=SchoolForm()
        return ECDO
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Inserted')
class SchoolFV(FormView):
    template_name='SchoolFV.html'
    form_class=SchoolForm
    def form_valid(self, form):
        form.save()
        return HttpResponse('Done')