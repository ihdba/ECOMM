from django.shortcuts import render, redirect


from .models import Product
from .forms import ProductForm

def index(request):

    products = Product.objects.all()
    context = {
        'title': 'ECOMM Products',
        'products': products,
    }

    return render(request, 'products/index.html', context=context)





def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('products')
            except:
                pass
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})