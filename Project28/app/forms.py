from django import forms
g=[['MALE','male'],['FEMALE','female']]
c=[('PYTHON','python'),('DJANGO','django')]
class StudentForm(forms.Form):
    sname=forms.CharField()
    id=forms.IntegerField()
    email=forms.EmailField()
    url=forms.URLField()
    address=forms.CharField(widget=forms.Textarea())
    password=forms.CharField(widget=forms.PasswordInput())
    # gender=forms.ChoiceField(choices=[('Male','male'),('Female','female')])
    # gender=forms.ChoiceField(choices=[('Male','male'),('Female','female')],widget=forms.RadioSelect)
    # course=forms.ChoiceField(choices=[('PY','PYTHON'),('DJ','DJANGO')])
    # course=forms.ChoiceField(choices=[('PY','PYTHON'),('DJ','DJANGO')],widget=forms.CheckboxSelectMultiple())
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)