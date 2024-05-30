from django.db.models import Q
from .models import Movie


def q_search(query):

    q_objects = Q()
    keywords = [word for word in query.split() if len(word) > 2]

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Movie.objects.filter(q_objects)
