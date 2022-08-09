from django.contrib import admin
from Pelicula.models import Peliculas, Review_pelicula, Playlist_basica_pelicula, Playlist_pelicula
# Register your models here.

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "genero")
    search_fields = ("nombre",)
    list_filter = ("genero",)

class Review_peliculaAdmin(admin.ModelAdmin):
    list_display = ("pelicula","owner")
    search_fields = ("owner", "pelicula")

class Playlist_basica_peliculaAdmin(admin.ModelAdmin):
    list_display = ("nombre","owner")
    list_filter = ("owner",)

class Playlist_peliculaAdmin(admin.ModelAdmin):
    list_display = ("playlist_iden","pelicula_iden")
    search_fields = ("playlist_iden","pelicula_iden")


admin.site.register(Peliculas,PeliculasAdmin)
admin.site.register(Review_pelicula,Review_peliculaAdmin)
admin.site.register(Playlist_basica_pelicula,Playlist_basica_peliculaAdmin)
admin.site.register(Playlist_pelicula,Playlist_peliculaAdmin)