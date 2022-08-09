from base64 import encode
from xml.dom.minidom import Notation
from django.db import models
from Usuarios.models import User

# Create your models here.
class Canciones(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    fecha = models.DateField()
    url = models.URLField(max_length=500)

    def __str__(self):
        return 'Cancion %s' % (self.nombre)

class Review_cancion(models.Model):
    cancion = models.ForeignKey(Canciones, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nota = models.FloatField()
    comentario = models.CharField(max_length=500) #widget=forms.Textarea()

    def __str__(self):
        return 'Comentario de %s a la cancion %s' % (self.owner, self.cancion)

class Playlist_basica_musica(models.Model):
    '''
    Sirve para crear una playlist.
    En términos practicos nos ayuda a verificar
    la existencia de una plylist, además podemos
    rescatar el nombre de una playlist según su id
    '''
    nombre = models.CharField(max_length=100)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'playlist %s del usuario %s' % (self.nombre, self.owner)
 
#PLaylist_basica contiene el id del usuario, podemos acceder a este gracias a 
#ese parámetro
class Playlist_musica(models.Model):
    musica_iden = models.ForeignKey(Canciones, on_delete=models.CASCADE, null=True)
    playlist_iden = models.ForeignKey(Playlist_basica_musica, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Relación entre %s con %s' % (self.musica_iden, self.playlist_iden)
