from django.shortcuts import render

# Create your views here.
def LoginForm(request):
    return render(request,'LoginForm.html')