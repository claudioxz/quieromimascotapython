# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from app_direccion.models import Comuna
from app_usuario.models import Usuario
from app_mascota.models import Mascota


TIPO_AVISO_CHOICES = (
    (1, 'Aviso Adopcion'),
    (2, 'Adoptar Mascota'),
    (3, 'Mascota Desaparecida'),
    (4, 'Mascota Encontrada'),
)


class Aviso(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='avisos', blank=True, null=True)
    descripcion = models.TextField()
    titulo = models.CharField(max_length=35, blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now=True, auto_created=True, blank=True)
    tipo_aviso = models.SmallIntegerField(choices=TIPO_AVISO_CHOICES)
    ubicacion = models.ForeignKey(Comuna, related_name='comuna')

    def get_tipo_aviso(self):
        return {'key': self.tipo_aviso, 'value': self.get_tipo_aviso_display()}

    def __unicode__(self):
        return self.titulo


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
    aviso = models.ForeignKey(Aviso, on_delete=models.CASCADE, related_name='imagenes')
    archivo = models.ImageField(upload_to='media/image')
