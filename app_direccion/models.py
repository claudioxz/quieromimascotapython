# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_usuario.models import Usuario


class Region(models.Model):
    nombre = models.CharField(max_length=300)


class Comuna(models.Model):
    nombre = models.CharField(max_length=300)
    region = models.ForeignKey(Region, related_name='comunas')


class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna)
    usuario = models.ForeignKey(Usuario)