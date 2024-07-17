
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.music, name = 'music'),
    path('add_music', views.add_music, name='add_music'),
]

