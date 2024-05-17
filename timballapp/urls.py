from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('post_paises', views.post_paises, name="post_paises"),
    path('post_equipos', views.post_equipos, name="post_equipos"),
    path('post_competiciones', views.post_competiciones, name="post_competiciones"),
    path('post_fixtures', views.post_fixtures, name="post_fixtures"),
    path('post_estadios', views.post_estadios, name="post_estadios"),
    path('post_bookmakers', views.post_bookmakers, name="post_bookmakers")
]
