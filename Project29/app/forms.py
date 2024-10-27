from django import forms
from app.models import *
class TopicForm(forms.Form):
    tn=forms.CharField()
class WebPageForm(forms.Form):
    tn=forms.ModelChoiceField(queryset=Topic.objects.all())
    nm=forms.CharField()
    ul=forms.URLField()
    el=forms.EmailField()
class AccessRecordForm(forms.Form):
    nm=forms.ModelChoiceField(queryset=WebPage.objects.all())
    au=forms.CharField()
    dt=forms.DateField()