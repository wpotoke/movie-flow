from django.urls import path
from . import views

app_name = "video_player"

urlpatterns = [
    path('film/<slug:slug_film>/watch/', views.film_player, name='film_player'),
    path('stream/film/<slug:slug_film>/<str:quality>/', views.stream_video, name='stream_video'),
    path('serial/<slug:slug_serial>/season/<int:season_number>/episode/<int:episode_number>/watch/', views.episode_player, name='episode_player'),
    path('stream/serial/<slug:slug_serial>/season/<int:season_number>/episode/<int:episode_number>/<str:quality>/', views.stream_serial, name='stream_serial'),
]
