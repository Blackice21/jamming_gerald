from django.shortcuts import render
from .models import Music, My_pictures
import audioread
# Create your views here.
def home(request):
    my_songs = Music.objects.all()
    picture = My_pictures.objects.all()[0]
    songs = my_songs.order_by('-song_date_added')
    context = {
        'songs':songs,
        'picture':picture,
    }
  
    return render(request, 'home.html', context)


            