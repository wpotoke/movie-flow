from django.db.models import Q
from .models import Movie, Serial


def q_search(query):

    if not query or len(query) < 3:
        return [], []

    q_objects = Q()
    keywords = [word for word in query.split() if len(word) > 2]

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    movies = Movie.objects.filter(q_objects)
    serials = Serial.objects.filter(q_objects)

    results = list(serials) + list(movies)

    labeled_results = []
    for result in results:
        if isinstance(result, Movie):
            labeled_results.append({'type': 'movie', 'object': result})
        elif isinstance(result, Serial):
            labeled_results.append({'type': 'serial', 'object': result})

    return labeled_results
