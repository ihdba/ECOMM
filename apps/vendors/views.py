from django.shortcuts import render

# Create your views here.



def index(request):

    context = {
        'title': 'ECOMM Vendors',
    }

    return render(request, 'vendors/index.html', context=context)