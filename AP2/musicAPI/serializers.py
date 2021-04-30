from rest_framework import serializers
from .models import Artista, Album, Cancion

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Artista
        
        fields = ['id' , 'name', 'age', 'albums', 'tracks', 'Self']
        #fields = {'id':'id' , 'name':'name', 'age':'age', 'albums':'albums', 'tracks':'tracks', 'self':'Self'}

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Album
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cancion
        fields = '__all__'


    

