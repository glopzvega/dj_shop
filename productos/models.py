# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre