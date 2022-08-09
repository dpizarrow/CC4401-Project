# -*- coding: utf-8 -*-
from Pelicula.models import Peliculas,Review_pelicula
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')
pelicula1 = Peliculas(nombre="Shrek",genero="Animada",fecha=datetime.date(2001, 7, 12),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/626aa2027030d9190567f704f7f12bab_53c80f27-d70d-4e93-93b2-312154041e19_480x.progressive.jpg?v=1573651553")
pelicula1.save()

pelicula2 = Peliculas(nombre="Toy Story",genero="Animada",fecha=datetime.date(1996, 1, 4),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/e2fc54358df39b0f3466d36d50684aa2_60d14fc6-696f-427e-9234-64dd666465a2_500x749.jpg?v=1573595133")
pelicula2.save()

pelicula3 = Peliculas(nombre="Spiderman",genero="Acción",fecha=datetime.date(2002, 5, 16),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/0221fffb41bd707803f61da0be3c6087_64c880a9-e91c-4a58-bfa8-bb61b1b6f726_480x.progressive.jpg?v=1573595153")
pelicula3.save()

pelicula4 = Peliculas(nombre="Joker",genero="Drama",fecha=datetime.date(2019, 10, 4),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/JOKER.PW.REP_480x.progressive.jpg?v=1574965207")
pelicula4.save()

pelicula5 = Peliculas(nombre="Mentiroso, mentiroso",genero="Comedia",fecha=datetime.date(1997, 3, 18),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/078e98aeb4a8376f613442716b4dd146_8eaa43cb-77aa-4a6f-8450-7dca95600749_480x.progressive.jpg?v=1573593643")
pelicula5.save()

pelicula6 = Peliculas(nombre="Mi Pobre Angelito",genero="Comedia",fecha=datetime.date(1990, 12, 25),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/dd43b3a44eacfd9ff0a3d97b311d17d2_b4766a06-e1c1-421d-acdb-3adae5c2c645_480x.progressive.jpg?v=1573652567")
pelicula6.save()

pelicula7 = Peliculas(nombre="Forrest Gump",genero="Drama",fecha=datetime.date(1994, 7, 6),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/forrest-gump---24x36_480x.progressive.jpg?v=1645558337")
pelicula7.save()

pelicula8 = Peliculas(nombre="El Conjuro",genero="Terror",fecha=datetime.date(2013, 8, 22),url="https://mx.web.img3.acsta.net/pictures/19/03/20/19/26/1988298.jpg")
pelicula8.save()

pelicula9 = Peliculas(nombre="Buscando a Nemo",genero="Animada",fecha=datetime.date(2019, 10, 4),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/a6417c7da7e7e30cb7565a63329cf1d7_5ee759e0-943f-46cb-a197-9174a3e85398_480x.progressive.jpg?v=1573587353")
pelicula9.save()

pelicula10 = Peliculas(nombre="Todopoderoso",genero="Comedia",fecha=datetime.date(2003, 5, 23),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/242ef1e695f3646388a5ca9e3077b483_b0930e88-c07d-4e1d-91e7-5d056bda5464_480x.progressive.jpg?v=1573618778")
pelicula10.save()

pelicula11 = Peliculas(nombre="Morbius",genero="Acción",fecha=datetime.date(2022, 4, 1),url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/morbius_qr2n41yx_480x.progressive.jpg?v=1644515385")
pelicula11.save()