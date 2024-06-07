from django.urls import path
from . import views

app_name = "video_player"

urlpatterns = [
    path('film/<slug:slug_film>/watch/', views.film_player, name='film-player'),
    path('serial/<slug:slug_serial>/watch/', views.serial_player, name='serial-player'),
    ]
