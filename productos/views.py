# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from models import Producto

def index(request):
    productos = Producto.objects.all()
    
    data = {
        "productos" : productos
    }
    
    return render(request, "productos/index.html", data)

def detail(request, pk):
    
    producto = get_object_or_404(Producto, pk=pk)
    
    data = {
        "producto" : producto
    }
    
    return render(request, "productos/detail.html", data)