
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('products/', include('apps.products.urls')),
    path('vendors/', include('apps.vendors.urls')),
    path('food/', include('apps.food.urls')),
]

