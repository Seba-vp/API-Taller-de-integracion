from rest_framework import viewsets
from . import models
from . import serializers

class ArtistaViewset(viewsets.ModelViewSet):
    queryset = models.Artista.objects.all()
    serializer_class = serializers.ArtistaSerializer

class AlbumViewset(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class CancionViewset(viewsets.ModelViewSet):
    queryset = models.Cancion.objects.all()
    serializer_class = serializers.CancionSerializer