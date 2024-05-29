from .models import Movie
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Value


def q_search(query):

    vector = SearchVector("name", "description")
    q = SearchQuery(query)

    result = (
        Movie.objects.annotate(rank=SearchRank(vector, q))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    return result

    # samopalniy variant
    # q_objects = Q()
    # keywords = [word for word in query.split() if len(word) > 2]

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return Movie.objects.filter(q_objects)
