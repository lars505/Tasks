from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Tasks(models.Model):
    titulo  = models.CharField(max_length=30)
    descripcion  = models.CharField(max_length=100)
    completado = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now =True)
    usuario = models.ForeignKey(User, on_delete =  models.CASCADE)
    imagen =  models.ImageField(default="default.jpg", blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.completado}"
    