from django.shortcuts import render, redirect


from .models import Producer
from .forms import ProducerForm

def index(request):

    producers = Producer.objects.all()
    context = {
        'title': 'ECOMM Producers',
        'producers': producers,
    }

    return render(request, 'producers/index.html', context=context)





def add_producer(request):
    if request.method == "POST":
        form = ProducerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('products')
            except:
                pass
    else:
        form = ProducerForm()

    return render(request, 'producers/add_producer.html', {'form': form})