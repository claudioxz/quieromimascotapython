# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_usuario.models import Usuario


class Region(models.Model):
    nombre = models.CharField(max_length=300)
    numero = models.CharField(max_length=4)

    def __unicode__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=300)
    region = models.ForeignKey(Region, related_name='provincias', null=True)

    def __unicode__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=300)
    codigo = models.CharField(max_length=300)
    provincia = models.ForeignKey(Provincia, related_name="comunas")

    def __unicode__(self):
        return self.nombre


class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna)
    usuario = models.ForeignKey(Usuario)

