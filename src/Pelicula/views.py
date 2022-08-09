from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Pelicula.models import Peliculas, Playlist_pelicula, Review_pelicula, Playlist_basica_pelicula
from Pelicula.forms import NuevaReviewPelicula
from django.db.models.functions import Replace
from django.db.models import Value, Q, Avg, F, Func
from django.core import serializers
from django.contrib.auth.decorators import login_required

from grupo6.settings import LOGIN_REDIRECT_URL

class Round(Func):
  function = 'ROUND'
  arity = 2

def pelicula_home_page(request):
    search = request.POST.get("buscar")
    ultimas_peliculas = Peliculas.objects.annotate(
        avg_score=Round(Avg('review_pelicula__nota'),2)).order_by('-avg_score')

    playlist = Playlist_basica_pelicula.objects.filter(
        Q(owner_id=request.user.id))

    if search:
        ultimas_peliculas = Peliculas.objects.filter(
            Q(nombre__icontains=search) |
            Q(genero__icontains=search)
        ).distinct()

    peliculas1 = Peliculas.objects.all().order_by("fecha").first()
    peliculas2 = Peliculas.objects.all().order_by("fecha").last()

    return render(request, "Pelicula/index.html", {'ultimas_peliculas': ultimas_peliculas, 'min': peliculas1.fecha.year, 'max': peliculas2.fecha.year, 'playlist': playlist})

@login_required(login_url=LOGIN_REDIRECT_URL)
def pelicula_make_review(request):
    pelicula  = Peliculas.objects.annotate(
        avg_score=Round(Avg('review_pelicula__nota'),2)).get(id=request.GET["id"])
    ultimas_review = Review_pelicula.objects.filter(pelicula=pelicula)
    print(ultimas_review)

    if request.method == "GET":
        pelicula  = Peliculas.objects.annotate(
        avg_score=Round(Avg('review_pelicula__nota'),2)).get(id=request.GET["id"])
        return render(request, "Pelicula/make_review.html", {"pelicula": pelicula, "ultimas_review": ultimas_review})

    if request.method == "POST":  # revisar si el método de la request es POST
        form_review = NuevaReviewPelicula(request.POST)
        if form_review.is_valid():
            nueva_tarea = form_review.save()  # save() de ModelForm
            if Review_pelicula.objects.filter(pelicula=pelicula, owner=request.user).exists():
                Rupdate = Review_pelicula.objects.filter(
                    pelicula=pelicula, owner=request.user)
                Rupdate.update(nota=Replace('nota', Value(
                    Rupdate[0].nota), Value(nueva_tarea.nota)))
                Rupdate.update(comentario=Replace('comentario', Value(
                    Rupdate[0].comentario), Value(nueva_tarea.comentario)))
            else:
                nueva_tarea.pelicula = pelicula
                nueva_tarea.owner = request.user
                nueva_tarea.save()  # save() de Model
        # if request.user.is_authenticated:
        pelicula  = Peliculas.objects.annotate(
        avg_score=Round(Avg('review_pelicula__nota'),2)).get(id=request.GET["id"])
        return render(request, "Pelicula/make_review.html", {"pelicula": pelicula, "ultimas_review": ultimas_review, "form_review": form_review})


def show_reviews_pelicula(request):

    all_reviews = Review_pelicula.objects.all()
    return render(request, "Pelicula/view_reviews.html", {"all_reviews": all_reviews})


def filtrar_peliculas(request):
    #is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == 'GET':

        name = request.GET["nombre"]
        fechas = request.GET["fecha"]
        fechas = fechas.split(',')
        # artista=request.GET["artista"]
        # genero=request.GET["genero"]
        # nota=request.GET["nota"]
        playlist = serializers.serialize(
            "json", Playlist_basica_pelicula.objects.filter(Q(owner_id=request.user.id)))
        # print(playlist)
        ultimas_peliculas = Peliculas.objects.annotate(
        avg_score=Avg('review_pelicula__nota')).order_by('-avg_score')
        query = Q(nombre__startswith=name)
        query.add(Q(genero__startswith=name), Q.OR)
        query.add(Q(fecha__year__range=fechas), Q.AND)
        ultimas_peliculas = ultimas_peliculas.filter(query)
        resp = []
        for l in ultimas_peliculas:
            fecha=l.fecha.strftime("%b. %#d, %Y")
            resp.append({'url': l.url, 'nombre': l.nombre, 'genero': l.genero,
                        'fecha': fecha, 'id': l.id, 'playlist': playlist})

        return JsonResponse({'context': resp})
    else:
        return HttpResponse({'status': 'Invalid request'}, status=400)


def add_pelicula_playlist(request):
    if request.method == 'GET':
        pelicula_id = request.GET["id"]
        pelicula = Peliculas.objects.get(id=pelicula_id)
        playlist_id = request.GET["playlist"]
        playlist = Playlist_basica_pelicula.objects.get(id=playlist_id)
        playlist_pelicula = Playlist_pelicula(
            pelicula_iden=pelicula, playlist_iden=playlist)
        if Playlist_pelicula.objects.filter(pelicula_iden=pelicula_id, playlist_iden=playlist_id).exists():
            return JsonResponse({'context': "Este Morbius ya está en la playlist"})

        playlist_pelicula.save()
        return JsonResponse({'context': "Pelicula agregada correctamente"})

    else:
        return HttpResponse({'status': 'Invalid request'}, status=400)

def nueva_playlist_pelicula(request):
    if request.method == 'GET':
        pelicula_id=request.GET["id"]
        pelicula = Peliculas.objects.get(id=pelicula_id)
        nombre_playlist=request.GET["nombre"]
        user=request.user
        if Playlist_basica_pelicula.objects.filter(Q(nombre=nombre_playlist,owner=user)).exists():
            return JsonResponse({'context': "Esta playlist ya existe"})
        new_playlist= Playlist_basica_pelicula(nombre=nombre_playlist,owner=user)
        new_playlist.save()
        playlist_pelicula = Playlist_pelicula(pelicula_iden = pelicula, playlist_iden = new_playlist)
        playlist_pelicula.save()
        return JsonResponse({'context': "Nueva playlist agregada correctamente"})
    else:
        return HttpResponse({'status': 'Invalid request'}, status=400)
