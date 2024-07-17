
# from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('products/', include('apps.products.urls')),
    path('vendors/', include('apps.vendors.urls')),
    path('food/', include('apps.food.urls')),
    path('producers/', include('apps.producers.urls')),
    path('locations/', include('apps.locations.urls')),
    path('blog/', include('apps.blog.urls')),
    path('music/', include('apps.music.urls')),
    path('dashboard/', include('apps.accounts.urls')),
]

