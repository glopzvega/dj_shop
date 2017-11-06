from django.conf.urls import url

import views

app_name = "productos"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<pk>[0-9]+)', views.detail, name="detail"),
]