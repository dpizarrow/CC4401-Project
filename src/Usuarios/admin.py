from django.contrib import admin

# Register your models here.
from Usuarios.models import User


admin.site.register(User)