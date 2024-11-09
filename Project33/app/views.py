from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'adi ANd AditYA Same', 'dt':dt, 'c':1}
    return render(request,'filters.html',d)
def myfilters(request):
    d={'data':'adi ANd AditYA Same'}
    return render(request,'myfilters.html',d)