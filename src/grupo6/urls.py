"""grupo6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django.urls import path
from Musica.views import *
from Pelicula.views import *
from Usuarios.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('test', test, name="test"),
    path('perfil', perfil_template, name="perfil"),
    path('homepage', homepage, name="home-page"),
    path('register', register_user_new, name="register_user_"),
    path('', login_user_new, name='login'),
    path('restore_password', restore_password, name="restore_password"),
    path('logout', logout_user, name='logout'),
    path('musica', musica_home_page, name='musica_home_page'),
    path('pelicula', pelicula_home_page, name='pelicula_home_page'),
    path('review_cancion', musica_make_review, name='review_cancion'),
    path('review_pelicula', pelicula_make_review, name='review_pelicula'),
    path('show_reviews_musica', show_reviews_musica, name='show_reviews_musica'),
    path('filtrar_canciones', filtrar_canciones, name='filtrar_canciones'),
    path('add_musica_playlist', add_musica_playlist, name='add_musica_playlist'),
    path('nueva_playlist_musica', nueva_playlist_musica, name='nueva_playlist_musica'),
    path('nueva_playlist_pelicula', nueva_playlist_pelicula, name='nueva_playlist_pelicula'),
    path('filtrar_peliculas', filtrar_peliculas, name='filtrar_peliculas'),
    path('add_pelicula_playlist', add_pelicula_playlist, name='add_pelicula_playlist'),
    path('show_reviews_peliula', show_reviews_pelicula,
         name='show_reviews_pelicula')
]
