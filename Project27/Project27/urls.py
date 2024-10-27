"""
URL configuration for Project27 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_school/',insert_school,name='insert_school'),
    path('insert_student/',insert_student,name='insert_student'),
    path('display_school/',display_school,name='display_school'),
    path('display_student/',display_student,name='display_student'),
    path('update_student/',update_student,name='update_student'),
    path('delete_student/',delete_student,name='delete_student'),
    path('insert_schoolform/',insert_schoolform,name='insert_schoolform'),
    path('insert_studentform/',insert_studentform,name='insert_studentform'),
]
