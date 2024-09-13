from django.urls import path
from RCB.views import *
urlpatterns=[
    path('captain/',captain,name='captain'),
]