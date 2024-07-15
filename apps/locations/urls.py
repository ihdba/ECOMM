# from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.locations, name='locations'),
    path('eat/', views.eat, name='eat'),
    path('stays/', views.stays, name='stays'),
]