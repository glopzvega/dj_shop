# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import Producto

@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "categoria", "precio", "cantidad")
