# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_usuario.models import Usuario
from app_mascota.models import Mascota


TIPO_AVISO_CHOICES = (
    (1, 'Aviso Adopcion'),
    (2, 'Aviso Adoptar'),
    (3, 'Aviso Desaparecida'),
    (4, 'Aviso Encontrada'),
)


class Aviso(models.Model):
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    descripcion = models.TextField()
    titulo = models.CharField(max_length=35, blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now=True, auto_created=True, blank=True)
    tipo_aviso = models.SmallIntegerField()


class AvisoAdopcion(Aviso):
    mascota = models.ForeignKey(Mascota, blank=True, null=True)


class AvisoAdoptar(Aviso):
    mascota = models.ForeignKey(Mascota, blank=True, null=True)


class AvisoDesaparecida(Aviso):
    mascota = models.ForeignKey(Mascota)
    fecha_desaparecida = models.DateField()
    lugar = models.CharField(max_length=150)


class AvisoEncontrada(Aviso):
    fecha_encontrada = models.DateField()
    lugar = models.CharField(max_length=150)


class Imagen(models.Model):
    aviso = models.ForeignKey(Aviso, on_delete=models.CASCADE)
    archivo = models.ImageField(upload_to='image')