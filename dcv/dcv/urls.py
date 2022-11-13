"""dcv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from dcv_questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('page1', views.page1, name='page1'),
    path('page2', views.page2, name='page2'),
    path('page3', views.page3, name='page3'),
    path('page4', views.page4, name='page4'),
    path('page5', views.page5, name='page5'),
    path('page6', views.page6, name='page6'),
    path('page7', views.page7, name='page7'),
    path('page8', views.page8, name='page8'),
    path('page9', views.page9, name='page9'),
    path('page10', views.page10, name='page10'),
    path('page11', views.page11, name='page11'),
    path('page12', views.page12, name='page12'),
    path('page13', views.page13, name='page13'),
    path('page14', views.page14, name='page14'),
]
