from django.db import models
import audioread

# Create your models here.
class Music(models.Model):
    song_file = models.FileField(upload_to='music/')
    song_name = models.CharField(default=song_file.name, max_length=200)
    song_duration = models.CharField(default='0', max_length=200)
    song_artist = models.CharField(default='no artist', max_length=200)
    song_date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.song_name

    def path(self):
        return 'media/'+self.song_file.path
    
    def get_audio(self):
        with audioread.audio_open(self.song_file.path) as f:
            self.song_duration = f.duration
        return self.song_duration
    
  
class My_pictures(models.Model):
      image = models.ImageField(upload_to='my_pics/')
    