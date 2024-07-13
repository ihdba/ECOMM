
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name = 'food'),
    path('add_channel/', views.add_channel, name = 'add_channel'),
]

