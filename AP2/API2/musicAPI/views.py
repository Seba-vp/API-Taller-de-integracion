from django.shortcuts import render
from django.http import JsonResponse

import json

from .models import Artista, Cancion, Album
#Aca parte lo de ninja
from ninja import Schema

from ninja import NinjaAPI

from typing import List

from django.views.decorators.csrf import csrf_exempt

from base64 import b64encode

api = NinjaAPI(csrf=False)


def coder(x):
    x = str(x)
    coded = b64encode(x.encode()).decode('utf-8')
    if len(coded) > 22:
        coded = coded[:22]

    return coded

def decoder(x):
    x = str(x)
    return x.split('+')[0]

base_url = 'http://127.0.0.1:8000/api/'



##### GET #####
#ARTISTAS
@api.api_operation(["GET","POST"],"/artists")
def list_artistas(request):
    if request.method == 'GET':
        qs = Artista.objects.all()
        l= []
        for a in qs:
            l.append(a.diccionario())
        return JsonResponse(l, safe=False)
    
    elif request.method == 'POST':
        body = json.load(request)

        if 'name' in body and 'age' in body:
            name = body['name']
            age = body['age']
            artist_id = coder(name)

            if Artista.objects.filter(id=artist_id).exists():
                data = 'Ya existe este artista'
                return JsonResponse(data,status = 409, safe=False)

            else:
                to_create = {
                    'id': artist_id,
                    'name': name, 
                    'age': age,
                    'albums': base_url+'atists/'+str(artist_id)+'/albums',
                    'tracks': base_url+'atists/'+str(artist_id)+'/tracks',
                    'Self': base_url+'atists/'+str(artist_id),
                    }
                artist = Artista.objects.create(**to_create)
                return JsonResponse(artist.diccionario(), status=201)
    
        else:
            data = 'Input invalido'
            return JsonResponse(data,status = 400, safe=False)



@api.api_operation(["GET","DELETE"],"/artists/{artist_id}")
def get_artist(request, artist_id):
    if Artista.objects.filter(id=artist_id).exists():
        a = Artista.objects.get(id=artist_id)
        
        if request.method == 'DELETE':
            a.delete()
            data = 'artista eliminado'
            return JsonResponse(data, status = 204, safe=False)
        else:
            return JsonResponse(a.diccionario(),status = 200)
    else:
        data = 'Artista no encontrado'
        return JsonResponse(data,status = 404, safe=False)




@api.api_operation(["GET","POST"],"/artists/{artist_id}/albums")
def get_artist_albums(request, artist_id):
   
    if request.method == 'GET':
        if Artista.objects.filter(id=artist_id).exists():
            artist = Artista.objects.get(id=artist_id)
            albums = Album.objects.all()
            album_list =  []
            for album in albums:
                if album.artist == artist.Self:
                    album_list.append(album.diccionario())
            return JsonResponse(album_list, safe=False)
        else:
            data = 'Artista no encontrado'
            return JsonResponse(data,status = 404, safe=False)
    
    elif request.method == 'POST':
        if Artista.objects.filter(id=artist_id).exists():
            body = json.load(request)
            if 'name' in body and 'genre' in body:
                name = body['name']
                genre = body['genre']
                album_id = coder(str(name)+':'+str(artist_id))

                if Album.objects.filter(id=album_id).exists():
                    data = 'Ya existe este album'
                    return JsonResponse(data,status = 409, safe=False)
                else:
                    to_create = {
                        'id': album_id,
                        'name': name, 
                        'genre': genre,
                        'artist': base_url+'atists/'+str(artist_id),
                        'tracks': base_url+'albums/'+str(album_id)+'/tracks',
                        'Self': base_url+'albums/'+str(album_id),
                        'artist_id': artist_id,
                        }
                    album = Album.objects.create(**to_create)
                    return JsonResponse(album.diccionario(), status=201)
            else:
                data = 'Input invalido'
                return JsonResponse(data,status = 400, safe=False)
        else:
            data = 'Artista no encontrado'
            return JsonResponse(data,status = 422, safe=False)


@api.get("/artists/{artist_id}/tracks")
def get_artist_tracks(request, artist_id):
    if Artista.objects.filter(id=artist_id).exists():
        artist = Artista.objects.get(id=artist_id)
        tracks = Cancion.objects.all()
        track_list =  []
        for track in tracks:
            if track.artist == artist.Self:
                track_list.append(track.diccionario())

        return JsonResponse(track_list, safe=False)
    else:
        data = 'Artista no encontrado'
        return JsonResponse(data,status = 404, safe=False)


#ALBUMS
@api.get("/albums")
def list_albums(request):
    qs = Album.objects.all()
    l= []
    for a in qs:
        l.append(a.diccionario())
    return JsonResponse(l, safe=False)

@api.get("/albums/{album_id}")
def get_album(request, album_id):
    if Album.objects.filter(id=album_id).exists():
        a = Album.objects.get(id=album_id)
        if reques.method == 'DELETE':
            a.delete()
            data = 'album eliminado'
            return JsonResponse(data, status = 204, safe=False)

        else:
            return JsonResponse(a.diccionario())
    else:
        data = 'Album no encontrado'
        return JsonResponse(data,status = 404, safe=False)


@api.api_operation(["GET","POST"],"/albums/{album_id}/tracks")
def get_album_tracks(request, album_id):
    if request.method == 'GET':
        if Album.objects.filter(id=album_id).exists():
            album = Album.objects.get(id=album_id)
            tracks = Cancion.objects.all()
            track_list =  []
            for track in tracks:
                if track.album == album.Self:
                    track_list.append(track.diccionario())
            return JsonResponse(track_list, safe=False)
        else:
            data = 'Album no encontrado'
            return JsonResponse(data,status = 404, safe=False)
        
       
    elif request.method == 'POST':
        if Album.objects.filter(id=album_id).exists():
            body = json.load(request)
            if 'name' in body and 'duration' in body:
                name = body['name']
                duration = body['duration']
                track_id = coder(str(name)+':'+str(album_id))

                if Cancion.objects.filter(id=track_id).exists():
                    data = 'Ya existe este track'
                    return JsonResponse(data,status = 409, safe=False)
                else:
                    album = Album.objects.get(id=album_id)

                    to_create = {
                        'id': track_id,
                        'name': name, 
                        'duration': duration,
                        'times_Played': 0,
                        'artist': base_url+'artists/'+str(album.artist_id),
                        'album': base_url+'albums/'+str(album_id),
                        'Self': base_url+'tracks/'+str(track_id),
                        'artist_id': album.artist_id,
                        'album_id': album_id,
                        }
                    
                    track = Cancion.objects.create(**to_create)
                    return JsonResponse(track.diccionario(), status= 201)
            else:
                data = 'Input invalido'
                return JsonResponse(data,status = 400, safe=False)
        else:
            data = 'Album no encontrado'
            return JsonResponse(data,status = 422, safe=False)
        
        
#TRACKS
@api.get("/tracks")
def list_tracks(request, album_id):
    qs = Cancion.objects.all()
    l = []

    for t in qs:
        l.append(t.diccionario())
    return JsonResponse(l , safe=False)

@api.get("/tracks/{track_id}")
def get_track(request, track_id):
    if Cancion.objects.filter(id=track_id).exists()::
        t = Track.objects.get(id=track_id)
        return JsonResponse(t.diccionario())
    else:
        data = 'Track no encontrado'
        return JsonResponse(data,status = 404, safe=False)
        


##### DELETE ####



##### PUT ####

