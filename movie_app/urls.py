from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('movies/', views.show_all_movie, name='movies'),
    path('movie/<slug:slug_movie>/', views.show_one_movie, name='movie-detail'),
    path('directors/', views.show_directors),
    path('director/<slug:slug_director>/', views.show_one_director, name='director_film'),
    path('actors/', views.show_actors, name='all_actors'),
    path('actor/<slug:slug_name>/', views.show_actor, name='actor_film'),
    ]
