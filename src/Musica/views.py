import re
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Musica.models import Canciones, Playlist_musica, Review_cancion, Playlist_basica_musica
from Musica.forms import NuevaReviewCancion
from django.db.models.functions import Replace
from django.db.models import Value, Q, Avg, F, Func
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Round

from grupo6.settings import LOGIN_REDIRECT_URL

class Round(Func):
  function = 'ROUND'
  arity = 2

def musica_home_page(request):
    search = request.POST.get("buscar")
    ultimas_canciones =  Canciones.objects.annotate(
        avg_score=Round(Avg('review_cancion__nota'), 2)).order_by('-avg_score')

    playlist = Playlist_basica_musica.objects.filter(
        Q(owner_id=request.user.id))

    if search:
        ultimas_canciones = Canciones.objects.filter(
            Q(nombre__icontains=search) |
            Q(artista__icontains=search)
        ).distinct()
    canciones1 = Canciones.objects.all().order_by("fecha").first()
    canciones2 = Canciones.objects.all().order_by("fecha").last()

    return render(request, "Musica/index.html", {'ultimas_canciones': ultimas_canciones, 'min': canciones1.fecha.year, 'max': canciones2.fecha.year, 'playlist': playlist})


@login_required(login_url=LOGIN_REDIRECT_URL)
def musica_make_review(request):
    cancion = Canciones.objects.annotate(
        avg_score=Round(Avg('review_cancion__nota'),2)).get(id=request.GET["id"])
    ultimas_review = Review_cancion.objects.filter(cancion=cancion)
    
    if request.method == "GET":
        cancion = Canciones.objects.annotate(
        avg_score=Round(Avg('review_cancion__nota'),2)).get(id=request.GET["id"])
        return render(request, "Musica/make_review.html", {"cancion": cancion, "ultimas_review": ultimas_review})
        

    if request.method == "POST":
        form_review = NuevaReviewCancion(request.POST)
        ##cancion = Canciones.objects.get(id=request.GET["id"])
        # if Review_cancion.objects.filter(cancion=cancion,owner=request.user).exists():
        ##   nueva_tarea= Review_cancion.objects.filter(cancion=cancion,owner=request.user)
        if form_review.is_valid():
            nueva_tarea = form_review.save()  # save() de ModelForm
            if Review_cancion.objects.filter(cancion=cancion, owner=request.user).exists():
                Rupdate = Review_cancion.objects.filter(
                    cancion=cancion, owner=request.user)
                # solo existe 1 comentario con el mismo usuario y cancion
                Rupdate.update(nota=Replace('nota', Value(
                    Rupdate[0].nota), Value(nueva_tarea.nota)))
                Rupdate.update(comentario=Replace('comentario', Value(
                    Rupdate[0].comentario), Value(nueva_tarea.comentario)))
            else:
                nueva_tarea.cancion = cancion
                nueva_tarea.owner = request.user
                nueva_tarea.save()
        # if request.user.is_authenticated:
        cancion = Canciones.objects.annotate(
        avg_score=Round(Avg('review_cancion__nota'),2)).get(id=request.GET["id"])
        return render(request, "Musica/make_review.html", {"cancion": cancion, "form_review": form_review, "ultimas_review": ultimas_review})


def show_reviews_musica(request):

    all_reviews = Review_cancion.objects.all()
    # view_review.html tiene busqueda con boton de busqueda, index.html tiene busqueda con ajax
    return render(request, "Musica/index.html", {"all_reviews": all_reviews})


def filtrar_canciones(request):
    #is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == 'GET':

        name = request.GET["nombre"]
        fechas = request.GET["fecha"]
        fechas = fechas.split(',')
        # artista=request.GET["artista"]
        # genero=request.GET["genero"]
        # nota=request.GET["nota"]
        playlist = serializers.serialize(
            "json", Playlist_basica_musica.objects.filter(Q(owner_id=request.user.id)))
        # print(playlist)
        ultimas_canciones = Canciones.objects.annotate(
        avg_score=Avg('review_cancion__nota')).order_by('-avg_score')
        query = Q(nombre__startswith=name)
        query.add(Q(genero__startswith=name), Q.OR)
        query.add(Q(album__startswith=name), Q.OR)
        query.add(Q(fecha__year__range=fechas), Q.AND)
        ultimas_canciones = ultimas_canciones.filter(query)
        resp = []
        for l in ultimas_canciones:
            fecha=l.fecha.strftime("%b. %#d, %Y")
            resp.append({'url': l.url, 'nombre': l.nombre, 'artista': l.artista, 'genero': l.genero,
                        'album': l.album, 'fecha': fecha, 'id': l.id, 'playlist': playlist})

        return JsonResponse({'context': resp})
    else:
        return HttpResponse({'status': 'Invalid request'}, status=400)


def add_musica_playlist(request):
    if request.method == 'GET':
        cancion_id = request.GET["id"]
        cancion = Canciones.objects.get(id=cancion_id)
        playlist_id = request.GET["playlist"]
        playlist = Playlist_basica_musica.objects.get(id=playlist_id)
        # user_id=request.user.id
        playlist_cancion = Playlist_musica(
            musica_iden=cancion, playlist_iden=playlist)
        if Playlist_musica.objects.filter(musica_iden=cancion_id, playlist_iden=playlist_id).exists():
            return JsonResponse({'context': "Esta canción ya está en la playlist"})

        playlist_cancion.save()
        return JsonResponse({'context': "Canción agregada correctamente"})
    else:
        return HttpResponse({'status': 'Invalid request'}, status=400)
    
def nueva_playlist_musica(request):
    if request.method == 'GET':
        cancion_id=request.GET["id"]
        cancion = Canciones.objects.get(id=cancion_id)
        nombre_playlist=request.GET["nombre"]
        user=request.user
        if Playlist_basica_musica.objects.filter(Q(nombre=nombre_playlist,owner=user)).exists():
            return JsonResponse({'context': "Esta playlist ya existe"})
        new_playlist= Playlist_basica_musica(nombre=nombre_playlist,owner=user)
        new_playlist.save()
        playlist_cancion = Playlist_musica(musica_iden = cancion, playlist_iden = new_playlist)
        playlist_cancion.save()
        return JsonResponse({'context': "Nueva playlist agregada correctamente"})
    else:
        return HttpResponse({'status': 'Invalid request'}, status=400)
