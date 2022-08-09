import imp
from xml.dom.minidom import Notation
from django.db import models
from Usuarios.models import User

# Create your models here.
class Peliculas(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    fecha = models.DateField()
    url = models.URLField(max_length=500)

    def __str__(self):
        return 'Pelicula %s' % (self.nombre)

class Review_pelicula(models.Model):
    ##llave foranea cancion id
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nota = models.FloatField()
    comentario = models.CharField(max_length=500)

    def __str__(self):
        return 'Comentario de %s a la pelicula %s' % (self.owner, self.pelicula)

class Playlist_basica_pelicula(models.Model):
    '''
    Sirve para crear una playlist.
    En términos practicos nos ayuda a verificar
    la existencia de una plylist, además podemos
    rescatar el nombre de una playlist según su id
    '''
    nombre = models.CharField(max_length=100)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    #usuario = 
    # Se puede rescatar el usuario¿?

    def __str__(self):
        return 'playlist %s del usuario %s' % (self.nombre, self.owner)

class Playlist_pelicula(models.Model):
    pelicula_iden = models.ForeignKey(Peliculas, on_delete=models.CASCADE, null=True)
    playlist_iden = models.ForeignKey(Playlist_basica_pelicula, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Relación entre %s con %s' % (self.pelicula_iden, self.playlist_iden)
