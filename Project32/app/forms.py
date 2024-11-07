from django import forms
from app.models import *
class StudentMF(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    remail=forms.EmailField()
    def clean(self):
        se=self.cleaned_data['semail']
        re=self.cleaned_data['remail']
        if se!=re:
            raise forms.ValidationError('Error')