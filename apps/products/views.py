from django.shortcuts import render


def index(request):

    context = {
        'title': 'ECOMM Products',
    }

    return render(request, 'products/index.html', context=context)