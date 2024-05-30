from django.shortcuts import render, get_object_or_404
from django.db.models import F, Count
from movie_app.utils import q_search
from .models import Movie, Director, Actor


def index(request):

    movies = Movie.objects.all()
    movies_slider = Movie.objects.all().order_by("-rating", "-rating_imdb", "-budget", "-name")
    

    context = {
        'movies': movies,
        'slider':movies_slider
    }

    return render(request, 'movie_app/index.html', context=context)

def show_all_movie(request):

    query = request.GET.get('search', None)

    if query:
        movies = q_search(query)
    else:
        movies = Movie.objects.order_by(F("rating").desc(nulls_last=True), F("name").asc(nulls_last=True), "-budget")
    
    agg = movies.aggregate(Count("name"))



    context = {
        "movies": movies,
        "aggregate_values": agg,
    }
    return render(request, "movie_app/all_movies.html", context=context)


def show_one_movie(request, slug_movie):
    movie = get_object_or_404(Movie, slug=slug_movie)

    context = {
        "movie": movie
        }
    
    return render(request, "movie_app/film.html", context=context)


def show_directors(request):
    director = Director.objects.order_by('first_name')

    context = {
        "directors": director
        }
    
    return render(request, "movie_app/directors.html", context=context)


def show_one_director(request, slug_director):
    director = get_object_or_404(Director, slug=slug_director)

    context = {
        "director": director
        }
    
    return render(request, "movie_app/one_director.html", context=context)


def show_actors(request):

    actors = Actor.objects.all()

    context = {
        'actors': actors
    }

    return render(request, 'movie_app/actors.html', context=context)


def show_actor(request, slug_name):
    actor = get_object_or_404(Actor, slug=slug_name)

    context = {
        "actor": actor
        }
    
    return render(request, "movie_app/one_actor.html", context=context)
