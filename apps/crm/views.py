from django.shortcuts import render

# Create your views here.



def dashboard(request):
    
    context = {
        
    }

    return render(request, 'crm/dashboard.html', context=context)


def register(request):
    
    context = {
        'title': 'ECOMM Dashboard |Register',
    }

    return render(request, 'crm/register.html', context=context)

def my_login(request):

    context = {
        'title': 'ECOMM Dashboard | Login',
    }

    return render(request, 'crm/my-login.html', context=context)




