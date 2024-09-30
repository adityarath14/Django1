from django.urls import path
from Food.views import *
app_name='Foodies'
urlpatterns=[
    path('Biriany/',Biriany,name='Biriany')
]