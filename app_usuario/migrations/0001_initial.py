# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-17 01:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creada', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('numero_celular', models.CharField(max_length=9)),
                ('numero_fijo', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth', to='app_usuario.Usuario')),
            ],
        ),
    ]
