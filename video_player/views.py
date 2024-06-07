from django.shortcuts import get_object_or_404, render
from movie_app.models import Movie, Serial

def film_player(request, slug_film):
    film = get_object_or_404(Movie, slug=slug_film)

    data = {"film": film}

    return render(request, 'video_player/film_player.html', context=data)


def serial_player(request, slug_serial):
    serial = get_object_or_404(Serial, slug=slug_serial)

    data = {"serial": serial}

    return render(request, '', context=data)