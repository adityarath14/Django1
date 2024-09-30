from django.urls import path
from CSK.views import *
urlpatterns=[
    path('captain/',captain,name='captain')
]