from django.shortcuts import render

# Create your views here.


def accounts(request):
    
    context = {
        'title': 'Acoounts dashboard',
    }
    return render(request, 'accounts/accounts.html', context=context)