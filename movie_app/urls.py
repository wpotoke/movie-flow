from django.urls import path
from . import views

app_name = "index"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('movies/', views.show_all_movie, name='movies'),
    path('movie/<slug:slug_movie>/', views.show_one_movie, name='movie-detail'),
    path('serials/', views.show_all_serial, name='serials'),
    path('serial/<slug:slug_serial>/', views.show_one_serial, name='serial-detail'),
    path('actors/', views.show_actors, name='all_actors'),
    path('actor/<slug:slug_name>/', views.show_actor, name='actor_film'),
    ]
