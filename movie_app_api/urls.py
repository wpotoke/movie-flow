from django.urls import path
from . import views

app_name = "movie_app_api"


urlpatterns = [
    path("", views.MovieList.as_view(), name="movies"),
    path("<slug:slug>/", views.MovieDetail.as_view(), name='movie-detail'),
    
]