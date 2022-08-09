import re
from urllib.request import Request
from django.db.models import Value, Q, Avg, F, Func
from django.shortcuts import render
from Pelicula.models import Peliculas, Review_pelicula, Playlist_pelicula, Playlist_basica_pelicula
from Usuarios.models import User
from Musica.models import Canciones, Review_cancion
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, ChangePasswordForm
from Musica.models import Playlist_basica_musica, Playlist_musica
from django import template

class Round(Func):
  function = 'ROUND'
  arity = 2


def perfil_template(request):
    current_user = request.user
    user_id = current_user.username
    user_email = current_user.correo
    #user_pronombre = current_user.pr

    user_playlist_musica = Playlist_basica_musica.objects.filter(
        owner=request.user.id)
    datos_musica = Playlist_musica.objects.all()

    user_playlist_pelicula = Playlist_basica_pelicula.objects.filter(
        owner=request.user.id)
    datos_pelicula = Playlist_pelicula.objects.all()

    context = {
        'user_id': user_id,
        'user_email': user_email,
        'user_playlist_musica': user_playlist_musica,
        'datos_musica': datos_musica,
        'user_playlist_pelicula': user_playlist_pelicula,
        'datos_pelicula': datos_pelicula,
    }

    return render(request, "perfil.html", context)


def test(request):
    return render(request, "base_listado.html")


def restore_password(request):
    context = {}
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(
                username=form.cleaned_data['user']).get()
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            return HttpResponseRedirect('/')
        else:
            context['form'] = form
            return render(request, "change_password.html", context)
    else:
        form = ChangePasswordForm()
        context['form'] = form
        return render(request, "change_password.html", context)


def register_user_new(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['user'], password=form.cleaned_data['password'],
                correo=form.cleaned_data['email'], pronombre=form.cleaned_data['pronombres'])
            return HttpResponseRedirect('/')
        else:
            context['form'] = form
            return render(request, "register.html", context)
    else:
        form = RegisterForm()
        context['form'] = form
        return render(request, "register.html", context)


def login_user_new(request):
    context = {
        'ultimas_canciones': Canciones.objects.all()[:6],
        'ultimas_peliculas': Peliculas.objects.all()[:6],
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, authenticate(
                username=form.cleaned_data['user'], password=form.cleaned_data['password']))
            return HttpResponseRedirect('/')
        else:
            context['form'] = form
            return render(request, "login.html", context)
    elif request.user.is_authenticated:
        return HttpResponseRedirect('/homepage')
    else:
        form = LoginForm()
        context['form'] = form
        return render(request, "login.html", context)


def homepage(request):
    mejores_peliculas = Peliculas.objects.annotate(
        avg_score=Round(Avg('review_pelicula__nota'), 2)).order_by('-avg_score')[:10]
    mejores_canciones = Canciones.objects.annotate(
        avg_score=Round(Avg('review_cancion__nota'),2)).order_by('-avg_score')[:10]
    context = {
        'mejores_peliculas': mejores_peliculas,
        'mejores_canciones': mejores_canciones,
    }
    return render(request, "home_page.html", context)


def logout_user(request):
    logout(request)
    # return render(request, 'login.html') cambio
    return HttpResponseRedirect('/')


def home_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('')
    else:
        return render(request, "Usuarios/index.html")
