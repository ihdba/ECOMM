
from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name = 'producers'),
    path('add_producer/', views.add_producer, name = 'add_producer'),
]

