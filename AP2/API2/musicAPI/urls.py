from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('artists/', views.artists, name="artists"),
    path('artists/<str:id>/', views.artists_id, name="artists"),

]
