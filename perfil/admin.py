from django.contrib import admin

from perfil.models import Perfil, UserHasPerfil

# Register your models here.
admin.site.register(Perfil)
admin.site.register(UserHasPerfil)