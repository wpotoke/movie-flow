from django.shortcuts import get_object_or_404, render
from movie_app.models import Movie, Serial
from django.http import StreamingHttpResponse
from .utils import open_file


def film_player(request, slug_film):
    film = get_object_or_404(Movie, slug=slug_film)
    data = {"film": film}
    return render(request, "video_player/film_player.html", context=data)


def serial_player(request, slug_serial):
    serial = get_object_or_404(Serial, slug=slug_serial)

    data = {"serial": serial}

    return render(request, "", context=data)

def stream_video(request, slug_film, quality):
    file, status_code, content_length, content_range = open_file(request, slug_film, quality)
    response = StreamingHttpResponse(file, status=status_code)
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Content-Type'] = 'video/mp4'
    if content_range:
        response['Content-Range'] = content_range
    return response
