from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.registrar_evento, name='registrar_evento'),
]