# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Create your views here.

from models import Producto

class IndexView(generic.ListView):
    template_name = "productos/index.html"
    context_object_name = "productos"
    
    def get_queryset(self):
        return Producto.objects.all()
    
class DetailView(generic.DetailView):
    model = Producto
    template_name = "productos/detail.html"

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

def agregar(request, pk):
    
    producto = get_object_or_404(Producto, pk=pk)
    
    producto.cantidad = producto.cantidad + 1
    
    producto.save()
    
    data = {
        "producto" : producto
    }
    
    return render(request, "productos/detail.html", data)

def quitar(request, pk):
    
    producto = get_object_or_404(Producto, pk=pk)
    
    producto.cantidad = producto.cantidad - 1
    
    producto.save()
    
    data = {
        "producto" : producto
    }
    
    return render(request, "productos/detail.html", data)


def nuevo(request):    
    return render(request, "productos/nuevo.html", {})

def editar(request, pk):   
    
    producto = get_object_or_404(Producto, pk=pk)
    
    data = {
        "producto" : producto
    }
    
    try:
        nombre = request.POST["nombre"]
        producto.nombre = nombre
        producto.save()        
        
        return render(request, "productos/detail.html", data)
        
    except:        
        pass
    
    return render(request, "productos/editar.html", data)

def guardar(request):  
    
    try:
        new = request.POST["nombre"]
    
    except (KeyError, "No se recibio el parametro nombre"):
        data = {
            "error_msj" : "No se pudo guardar el registro"
        }
        
        return render(request, 'productos/nuevo.html', data)
    
    else:    
        producto = Producto(nombre=new)
        producto.save()
    
    return HttpResponseRedirect(reverse('productos:detail', args=(producto.id,)))


