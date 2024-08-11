from django.shortcuts import get_object_or_404, render
from movie_app.models import Movie, Serial, Episode
from django.http import StreamingHttpResponse
from .utils import open_file

def film_player(request, slug_film):
    film = get_object_or_404(Movie, slug=slug_film)
    data = {"film": film}
    return render(request, "video_player/film_player.html", context=data)

def episode_player(request, slug_serial, season_number, episode_number):
    serial = get_object_or_404(Serial, slug=slug_serial)
    episode = get_object_or_404(Episode, serial=serial, season_number=season_number, episode_number=episode_number)
    data = {
        "serial": serial,
        "episode": episode
    }
    return render(request, "video_player/episode_player.html", context=data)

def stream_video(request, slug_film, quality):
    file, status_code, content_length, content_range = open_file(request, slug_film, quality)
    response = StreamingHttpResponse(file, status=status_code)
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Content-Type'] = 'video/mp4'
    if content_range:
        response['Content-Range'] = content_range
    return response

def stream_serial(request, slug_serial, season_number, episode_number, quality):
    episode = get_object_or_404(Episode, serial__slug=slug_serial, season_number=season_number, episode_number=episode_number)
    file, status_code, content_length, content_range = open_file(request, episode.slug, quality)
    response = StreamingHttpResponse(file, status=status_code)
    response['Accept-Ranges'] = 'bytes' 
    response['Content-Length'] = str(content_length)
    response['Content-Type'] = 'video/mp4'
    if content_range:
        response['Content-Range'] = content_range
    return response
