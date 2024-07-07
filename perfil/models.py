from django.db import models
from django.contrib.auth.models import User as DjangoUser  

class Perfil(models.Model):
    perfil = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.perfil

class UserHasPerfil(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.perfil.perfil}"

    class Meta:
        verbose_name = "Usuário com Perfil"
        verbose_name_plural = "Usuários com Perfis"
