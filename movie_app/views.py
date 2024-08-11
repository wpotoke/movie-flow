from django.shortcuts import render, get_object_or_404
from django.db.models import F
from movie_app.utils import q_search
from .models import Movie, Director, Actor, Serial



def index(request):

    movies = Movie.objects.all()
    movies_slider = Movie.objects.all().order_by(
        "-rating", "-rating_imdb"
    )[:7]

    context = {"movies": movies, "slider": movies_slider}

    return render(request, "movie_app/index.html", context=context)

def search(request):
    query = request.GET.get('q')
    results = q_search(query)

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'movie_app/search_results.html', context)

def show_all_movie(request):

    movies = Movie.objects.order_by(
            F("rating").desc(nulls_last=True), F("name").asc(nulls_last=True), "-budget"
        )

    context = {
        "movies": movies
    }
    return render(request, "movie_app/all_movies.html", context=context)


def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)

    context = {"movie": movie}

    return render(request, "movie_app/film.html", context=context)


def show_all_serial(request):
        
    serials = Serial.objects.order_by(
            F("rating").desc(nulls_last=True), F("name").asc(nulls_last=True), "-budget"
        )

    context = {
        "serials": serials,
        }
    return render(request, "movie_app/all_serials.html", context=context)


def show_one_serial(request, slug_serial):
    serial = get_object_or_404(Serial, slug=slug_serial)
    episodes = serial.episodes.all().order_by('pk')
    context = {"serial": serial, "episodes": episodes}

    return render(request, "movie_app/serial.html", context=context)


def show_directors(request):
    director = Director.objects.order_by("first_name")

    context = {"directors": director}

    return render(request, "movie_app/directors.html", context=context)


def show_one_director(request, slug_director):
    director = get_object_or_404(Director, slug=slug_director)

    context = {"director": director}

    return render(request, "movie_app/one_director.html", context=context)


def show_actors(request):

    actors = Actor.objects.all()

    context = {"actors": actors}

    return render(request, "movie_app/actors.html", context=context)


def show_actor(request, slug_name):
    actor = get_object_or_404(Actor, slug=slug_name)

    context = {"actor": actor}

    return render(request, "movie_app/one_actor.html", context=context)
