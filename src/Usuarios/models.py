from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pronombres = [('La', 'La'), ('El', 'El'), ('Le', 'Le'), ('Otro', 'Otro')]
    pronombre = models.CharField(max_length=5, choices=pronombres)
    # User por defecto tiene un campo email, pa que
    # usamos este? gustavo
    correo = models.EmailField(max_length=50)
    #username = models.CharField(max_length=50)
    # Django ID
