from django.contrib import admin
from Musica.models import Canciones, Review_cancion, Playlist_musica, Playlist_basica_musica
# Register your models here.

class CancionesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "artista","genero")
    search_fields = ("nombre", "artista")
    list_filter = ("genero",)

class Review_cancionAdmin(admin.ModelAdmin):
    list_display = ("cancion","owner")
    search_fields = ("owner", "cancion")

class Playlist_basica_musicaAdmin(admin.ModelAdmin):
    list_display = ("nombre","owner")
    list_filter = ("owner",)

class Playlist_musicaAdmin(admin.ModelAdmin):
    list_display = ("playlist_iden","musica_iden")
    search_fields = ("playlist_iden","musica_iden")


admin.site.register(Canciones,CancionesAdmin)
admin.site.register(Review_cancion,Review_cancionAdmin)
admin.site.register(Playlist_basica_musica,Playlist_basica_musicaAdmin)
admin.site.register(Playlist_musica,Playlist_musicaAdmin)