from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='artist-images/', blank=True, null=True)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100, default='---', blank=True, null=True)
    song_title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='song-files/')
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
