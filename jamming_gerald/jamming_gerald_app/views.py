from django.shortcuts import render
from .models import Music
import audioread
# Create your views here.
def home(request):
    my_songs = Music.objects.all()
    songs = my_songs.order_by('song_date_added')
    context = {
        'songs':songs,
    }
  
    return render(request, 'home.html', context)

            