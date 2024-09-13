from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Aditya','age':23}
    return render(request,'JinjaPrint.html',context=d)