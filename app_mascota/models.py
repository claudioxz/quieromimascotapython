# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

GENERO_CHOICE = (
    (1, 'Macho'),
    (2, 'Hembra')
)


class Tipo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre


class Raza(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='razas')

    def __unicode__(self):
        return self.nombre


class Mascota(models.Model):
    genero = models.SmallIntegerField(choices=GENERO_CHOICE)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    raza = models.OneToOneField(Raza, blank=True, null=True)
    edad = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.nombre


