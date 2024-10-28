from django import forms
from app.models import *
class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebPageModelForm(forms.ModelForm):
    class Meta:
        model=WebPage
        #fields='__all__'
        #fields=['email']
        exclude=['url']
        labels={'topic_name':'TN','name':'N'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}
        help_texts={'topic_name':'Parent Table Data'}
class AccessRecordModelForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'