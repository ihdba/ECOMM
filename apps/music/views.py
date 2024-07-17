from django.shortcuts import render, redirect

# Create your views here.


from .models import Music
from .forms import MusicForm

def music(request):

    mvideos = Music.objects.all()
    context = {
        'mvideos':mvideos,
    }

    return render(request, 'music/music.html', context=context)



def add_music(request):
    if request.method == "POST":
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('music')
            except:
                pass
    else:
        form = MusicForm()

    return render(request, 'music/add_music.html', {'form': form})