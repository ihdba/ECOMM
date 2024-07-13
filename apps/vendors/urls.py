
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name = 'vendors'),
    path('add_vendor/', views.add_vendor, name = 'add_vendor'),
]

