from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('post_paises', views.post_paises, name="post_paises"),
]
