from django.db import models

# Create your models here.

class Artista(models.Model):
    id = models.CharField(max_length=100, default=None, primary_key=True)
    name = models.CharField(max_length=100, default=None)
    age = models.IntegerField(default=None)
    albums = models.URLField(default=None)
    tracks = models.URLField( default=None)
    Self = models.URLField(default=None)


    def diccionario(self):
        return {'id': self.id , 'name': self.name, 'age':self.age, 'albums':self.albums, 'tracks':self.tracks, 'self':self.Self }

class Album(models.Model):
    id = models.CharField(max_length=100, default=None, primary_key=True)
    name = models.CharField(max_length=100, default=None)
    genre = models.CharField(max_length=100, default=None)
    artist = models.URLField(default=None)
    tracks = models.URLField(default=None)
    Self = models.URLField(default=None)
    artist_id = models.CharField(max_length=100, default=None, blank=True)
    ar_fk = models.ForeignKey(Artista, on_delete=models.CASCADE, default=None)


    def diccionario(self):
        return {'id': self.id , 'name': self.name, 'genre':self.genre, 'artist':self.artist, 'tracks':self.tracks, 'self':self.Self }


class Cancion(models.Model):
    id = models.CharField(max_length=100, default=None, primary_key=True)
    name = models.CharField(max_length=100, default=None)
    duration = models.FloatField(default=None)
    times_played = models.IntegerField(default=None)
    artist = models.URLField(default=None)
    album = models.URLField(default=None)
    Self = models.URLField(default=None)
    artist_id = models.CharField(max_length=100, default=None, blank=True)
    album_id = models.CharField(max_length=100, default=None, blank=True)
    ar_fk = models.ForeignKey(Artista, on_delete=models.CASCADE, default=None)
    al_fk = models.ForeignKey(Album, on_delete=models.CASCADE, default=None)



    def diccionario(self):
        return {'id': self.id , 'name': self.name, 'duration':self.duration, 'times_played':self.times_played, 'artist':self.artist, 'album':self.album, 'self':self.Self }


    def diccionario_no_id(self):
        return {'name': self.name, 'duration':self.duration, 'times_played':self.times_played, 'artist':self.artist, 'album':self.album, 'self':self.Self }
