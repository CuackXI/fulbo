from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name="Home"),
    path('feed', views.fixtures, name="feed"),
    path('fixture_detalle/<int:id>/', views.fixture_detalle),
    path('post_paises', views.post_paises, name="post_paises"),
    path('post_equipos', views.post_equipos, name="post_equipos"),
    path('post_competiciones', views.post_competiciones, name="post_competiciones"),
    path('post_fixtures', views.post_fixtures, name="post_fixtures"),
    path('post_estadios', views.post_estadios, name="post_estadios"),
    path('post_bookmakers', views.post_bookmakers, name="post_bookmakers"),
    path('post_apuestas', views.post_apuestas, name="post_apuestas"),
    path('post_apuestas_id', views.post_apuestas_id, name="post_apuestas_id")
]