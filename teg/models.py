from django.db import models

# Create your models here.

class usuario (models.Model):
    usuario = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Apodo = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def crear_usuario(self,usr,ape,apo,em,pas):
        self.usuario = usr
        self.Apellido = ape
        self.Apodo = apo
        self.Email = em
        self.password = pas

class partida (models.Model):
    partida = models.IntegerField
    nombre = models.CharField(max_length=30)
    administrador = models.ForeignKey(usuario,on_delete=models.CASCADE)

class equipos (models.Model):
    id_equipo = models.IntegerField
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    partida = models.ForeignKey(partida,on_delete=models.CASCADE)

class estadistica(models.Model):
    estadistica= models.IntegerField
    usuario_est=models.ForeignKey(usuario,on_delete=models.CASCADE)
    puntos = models.IntegerField
