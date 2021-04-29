from django.shortcuts import render
from django.http import JsonResponse



from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Artista, Cancion, Album
from .serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'artists':'lsit of artists',
        'albums' : 'list of albums',
        'track': 'a track',
        }
    return Response(api_urls)



#ARTISTA
@api_view(['GET', 'POST'])
def artists(request):
    
    if request.method == 'POST':
        print(type(request.data))
        data = request.data
        data['Self'] = data.pop['self']

        data = Response(data)

        serializer = ArtistaSerializer(data)
        if serializer.is_valid():
            print('entrooooo')
            serializer.save()
        return Response(serializer.data)
    else:
        artists = Artista.objects.all()

        for a in artists:
            pass

        serializer = ArtistaSerializer(artists, many=True)

        print(Response(serializer.data))
        return Response(serializer.data)

@api_view(['GET'])
def artists_id(request, id):
    artists = Artista.objects.all()
    serializer = ArtistaSerializer(artists, many=False)
    return Response(serializer.data)

