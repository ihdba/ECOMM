from django.shortcuts import render

# Create your views here.



def home(request):

    context = {
        'title': 'ECOMM Portal',
    }

    return render(request, 'portal/index.html', context=context)



def about(request):

    context = {
        'title': 'ECOMM About Us',
    }

    return render(request, 'portal/about.html', context=context)



def contact(request):

    context = {
        'title': 'ECOMM Contact Us',
    }

    return render(request, 'portal/contact.html', context=context)