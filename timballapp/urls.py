from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name="Home"),
    path('about', views.about, name="About"),
    path('Registrarse', views.signup, name="Signup"),
    path('IniciarSesion', views.login, name="Login"),
    path('fixture/<int:id>/', views.fixture_detalle),
    path('fixture_predicts/<int:id>/', views.fixture_predicts),
    path('equipo/<int:id>/', views.equipo_especifico,),
    path('busqueda/<str:query>/', views.feed_busqueda),

    # Estas no son urls del usuario hay que ver como hacer esto sin urls
    path('post_paises', views.post_paises, name="post_paises"),
    path('post_equipos', views.post_equipos, name="post_equipos"),
    path('post_competiciones', views.post_competiciones, name="post_competiciones"),
    path('post_fixtures', views.post_fixtures, name="post_fixtures"),
    path('post_estadios', views.post_estadios, name="post_estadios"),
    path('post_bookmakers', views.post_bookmakers, name="post_bookmakers"),
    path('post_apuestas', views.post_apuestas, name="post_apuestas"),
    path('post_apuestas_id', views.post_apuestas_id, name="post_apuestas_id"),
    path('post_porcentajes', views.post_porcentajes, name="post_porcentajes")
]