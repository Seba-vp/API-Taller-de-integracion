from django.urls import path
from . import views

urlpatterns = [
    path('', views.api.urls, name="api-overview"),


    #GET
    path('artists/', views.list_artistas, name="artists"),
    path('artists/<artist_id>', views.get_artist, name="artist"),
    path('artists/<artist_id>/albums', views.get_artist_albums, name="artist"),
    path('artists/<artist_id>/tracks', views.get_artist_tracks, name="artist"),
   
    path('albums/', views.list_albums, name="albums"),
    path('albums/<album_id>', views.get_album, name="album"),
    path('albums/<album_id>/tracks', views.get_album_tracks, name="album"),
    
    path('tracks/', views.list_tracks, name="track"),
    path('tracks/<track_id>', views.get_track, name="track"),
  



]
