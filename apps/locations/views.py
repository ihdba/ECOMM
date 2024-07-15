from django.shortcuts import render

# Create your views here.


def locations(request):
    
    return render(request, 'locations/locations.html')


def eat(request):
    
    return render(request, 'locations/eat.html')




def stays(request):
    
    return render(request, 'locations/stays.html')