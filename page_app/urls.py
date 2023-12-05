"""
URL configuration for samuka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render
from page_app.views import home, main, index, footer, header, sobre_mim, contato

urlpatterns = [
    path('', index),
    path('sobre_mim/', sobre_mim),
    path('header/', header),
    path('home/', home),
    path('contato/', contato),
    path('footer/', footer),
    path('main/', main),
]
