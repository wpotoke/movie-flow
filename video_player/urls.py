from django.urls import path
from . import views

app_name = "video_player"

urlpatterns = [
    path('film/<slug:slug_film>/watch/', views.film_player, name='film-player'),
    path('stream/<slug:slug_film>/<str:quality>/', views.stream_video, name='stream_video'),
    path('serial/<slug:slug_serial>/watch/', views.serial_player, name='serial-player'),
    # path('stream/<slug:slug_serial>/<str:quality>/', views.?, name='stream_serial'),
    ]
