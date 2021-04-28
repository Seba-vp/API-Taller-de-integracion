from django.db import models

# Create your models here.

class Artista(models.Model):
    id = models.CharField(max_length=100, default=None, primary_key=True)
    name = models.CharField(max_length=100, default=None)
    age = models.IntegerField(default=None)
    albums = models.URLField(default=None)
    tracks = models.URLField( default=None)
    Self = models.URLField(default=None)

class Album(models.Model):
    id = models.CharField(max_length=100, default=None, primary_key=True)
    name = models.CharField(max_length=100, default=None)
    genre = models.CharField(max_length=100, default=None)
    artist = models.URLField(default=None)
    tracks = models.URLField(default=None)
    Self = models.URLField(default=None)

class Cancion(models.Model):
    id = models.CharField(max_length=100, default=None, primary_key=True)
    name = models.CharField(max_length=100, default=None)
    duration = models.FloatField(default=None)
    times_Played = models.IntegerField(default=None)
    artist = models.URLField(default=None)
    album = models.URLField(default=None)
    Self = models.URLField(default=None)

