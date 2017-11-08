from django.conf.urls import url

import views

app_name = "productos"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<pk>[0-9]+)/agregar', views.agregar, name="agregar"),
    url(r'^(?P<pk>[0-9]+)/quitar', views.quitar, name="quitar"),
     
    url(r'^nuevo/', views.nuevo, name="nuevo"),
    
    url(r'^(?P<pk>[0-9]+)/actualizar/', views.editar, name="editar"),    
    url(r'^(?P<pk>[0-9]+)', views.detail, name="detail"),
    
    url(r'^guardar/', views.guardar, name="guardar"),    
]