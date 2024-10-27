from django import forms
from app.models import *
class TopicForm(forms.Form):
    tn=forms.CharField(label='Topic Name')
class WebPageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=Topic.objects.all(),label='Topic Name')
    nm=forms.CharField(label='Name')
    ul=forms.URLField(label='URL')
    el=forms.EmailField(label='Email')
class AccessRecordForm(forms.Form):
    nm=forms.ModelChoiceField(queryset=WebPage.objects.all(),label='Name')
    au=forms.CharField(label='Author')
    dt=forms.DateField(label='Date')