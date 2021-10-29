from django.shortcuts import render
from .models import Music, My_pictures
import audioread
# Create your views here.
def home(request):
    my_songs = Music.objects.all()
    songs = my_songs.order_by('-song_date_added')
    picture = My_pictures.objects.all()
    context = {
        'songs':songs,
        'picture':picture,
    }
  
    return render(request, 'home.html', context)


            