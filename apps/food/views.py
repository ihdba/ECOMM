from django.shortcuts import render

# Create your views here.



def index(request):

    context = {
        'title': 'ECOMM Food Stories',
    }

    return render(request, 'food/index.html', context=context)