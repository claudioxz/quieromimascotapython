# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    numero_celular = models.CharField(max_length=9)
    numero_fijo = models.CharField(max_length=9)
    fecha_creada = models.DateTimeField(auto_created=True, auto_now_add=True, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.nombre, self.apellido)


class UsuarioAuth(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    usuario = models.OneToOneField(Usuario, related_name='auth')

    def __unicode__(self):
        return self.usuario
