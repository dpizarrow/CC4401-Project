# -*- coding: utf-8 -*-
from Musica.models import Canciones,Review_cancion
import datetime
from Usuarios.models import User
import sys

sys.stdout.reconfigure(encoding='utf-8')
cancion1 = Canciones(nombre="Billie Jean",artista="Michael Jackson",genero="Pop",album="Thriller",fecha=datetime.date(1983, 1, 2),url="https://t2.genius.com/unsafe/327x327/https%3A%2F%2Fimages.genius.com%2Fac62751e0e513fa0ed16291e51790d08.953x953x1.jpg")
cancion1.save()

cancion2 = Canciones(nombre="Bohemian Rhapsody",artista="Queen",genero="Rock",album="A Night at the Opera",fecha=datetime.date(1975, 10, 31),url="https://t2.genius.com/unsafe/327x327/https%3A%2F%2Fimages.genius.com%2Fff9ddef65ab95da61354ce587748e2e9.600x600x1.png")
cancion2.save()

cancion3 = Canciones(nombre="Take on Me",artista="A-ha",genero="Pop Rock",album="Hunting High and Low",fecha=datetime.date(1984, 10, 19),url="https://t2.genius.com/unsafe/277x277/https%3A%2F%2Fimages.genius.com%2F8a6e8ab8f96e4a9ac1a0ab0b3ce1be01.600x600x1.jpg")
cancion3.save()

cancion4 = Canciones(nombre="Llamado de Emergencia",artista="Daddy Yankee",genero="Reggaetón",album="Talento de Barrio",fecha=datetime.date(2008, 9, 23),url="https://t2.genius.com/unsafe/327x327/https%3A%2F%2Fimages.genius.com%2F74e549a1adf990928cc344e61e2716d8.1000x1000x1.png")
cancion4.save()

cancion5 = Canciones(nombre="Cuéntale",artista="Don Omar",genero="Reggaetón",album="King of Kings",fecha=datetime.date(2003, 5, 2),url="https://t2.genius.com/unsafe/301x301/https%3A%2F%2Fimages.genius.com%2Fb6519cfe75d51ae8eb8198fe76cca526.500x500x1.jpg")
cancion5.save()

cancion6 = Canciones(nombre="Let it Be",artista="The Beatles",genero="Rock psicodélico",album="Let it Be",fecha=datetime.date(1970, 5, 8),url="https://t2.genius.com/unsafe/309x312/https%3A%2F%2Fimages.genius.com%2F38df3b59f231f4babd59aec795764979.494x500x1.jpg")
cancion6.save()

cancion7 = Canciones(nombre="Here Comes the Sun",artista="The Beatles",genero="Rock psicodélico",album="Abbey Road",fecha=datetime.date(1969, 9, 26),url="https://t2.genius.com/unsafe/327x327/https%3A%2F%2Fimages.genius.com%2F003c2b3d4b489659367e9fc1c47ffb62.1000x1000x1.png")
cancion7.save()

cancion8 = Canciones(nombre="Blackbird",artista="The Beatles",genero="Rock psicodélico",album="The Beatles (The White Album)",fecha=datetime.date(1969, 6, 11),url="https://t2.genius.com/unsafe/317x317/https%3A%2F%2Fimages.genius.com%2F85f5a0ea6444f048f35ac401fc26e633.1000x1000x1.png")
cancion8.save()

cancion9 = Canciones(nombre="Sin Gamulán",artista="Los Abuelos de la Nada",genero="Rock",album="Los Abuelos de la Nada",fecha=datetime.date(1982, 10, 15),url="https://t2.genius.com/unsafe/327x327/https%3A%2F%2Fimages.genius.com%2F908f316c490c4aa54b1db8813f5522da.400x400x1.jpg")
cancion9.save()

cancion10 = Canciones(nombre="¿Por qué no se van?",artista="Los Prisioneros",genero="Rock",album="Pateando Piedras",fecha=datetime.date(1986, 9, 15),url="https://t2.genius.com/unsafe/327x327/https%3A%2F%2Fimages.genius.com%2F53cd96a37617f23900f5c15b289cf75f.953x953x1.jpg")
cancion10.save()