from django.contrib import admin
from django.urls import path, include
from . views import*

urlpatterns = [
    path('', homepage, name='home'),
    # path('', ThingMultiplePKViewSet.as_view({'get': 'list'}), name='home'),
]
