from django.urls import path
from Bike.views import *
app_name='Travling'
urlpatterns=[
    path('Honda/',Honda,name='Honda')
]