from musicAPI.viewsets import ArtistaViewset, AlbumViewset, CancionViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('artists', ArtistaViewset)
router.register('albums', AlbumViewset)
router.register('tracks', CancionViewset)

#localhost:p/api/