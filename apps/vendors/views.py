from django.shortcuts import render, redirect

# Create your views here.


from .models import Vendor
from .forms import VendorForm


def index(request):

    vendors = Vendor.objects.all()
    context = {
        'title': 'ECOMM Vendors',
        'vendors': vendors,
    }

    return render(request, 'vendors/index.html', context=context)



def add_vendor(request):
    if request.method == "POST":
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('vendors')
            except:
                pass
    else:
        form = VendorForm()

    return render(request, 'vendors/add_vendor.html', {'form': form})