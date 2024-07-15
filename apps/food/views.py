from django.shortcuts import render, redirect

# Create your views here.

from .models import Food_Channel
from .forms import FoodChanneForm

def index(request):

    foodies = Food_Channel.objects.all()
    context = {
        'foodies':foodies,
    }

    return render(request, 'food/index.html', context=context)



def add_channel(request):
    if request.method == "POST":
        form = FoodChanneForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('food')
            except:
                pass
    else:
        form = FoodChanneForm()

    return render(request, 'food/add_channel.html', {'form': form})