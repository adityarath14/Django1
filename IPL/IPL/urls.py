"""
URL configuration for IPL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CSK.views import *
from RCB.views import *
from MI.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('MSD/',MSD,name='MSD'),
    path('Raina/',Raina,name='Raina'),
    path('Virat/',Virat,name='Virat'),
    path('ABD/',ABD,name='ABD'),
    path('Rohit/',Rohit,name='Rohit'),
    path('Hardhik/',Hardhik,name='Hardhik'),
]
