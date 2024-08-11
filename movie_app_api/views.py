from rest_framework import generics  # viewsets, mixins,
from rest_framework.pagination import PageNumberPagination

# from rest_framework.authentication import TokenAuthentication
from movie_app_api.permissions import IsAdminOrReadOnly
from movie_app.models import Movie
from .serializers import MovieSerializer


# class MovieViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    viewsets.GenericViewSet):

#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

class MovieAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 100

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieAPIListPagination


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "slug"
    permission_classes = (IsAdminOrReadOnly,)
    # authentication_classes = (TokenAuthentication, ) # allow enter only per token


# from functools import partial
# from django.core.serializers import serialize
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from movie_app.models import Movie
# from .serializers import MovieSerializer


# class MovieList(APIView):
#     def get(self, request, format=None):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MovieDetail(APIView):

#     def get_object(self, slug):
#         try:
#             return Movie.objects.get(slug=slug)
#         except Movie.DoesNotExist:
#             raise Http404

#     def get(self, request, slug, format=None):
#         movie = self.get_object(slug)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def put(self, request, slug, format=None):
#         movie = self.get_object(slug)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_velid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def path(self, request, slug, format=None):
#         movie = self.get_object(slug)
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_velid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug, format=None):
#         movie = self.get_object(slug)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import mixins
# from rest_framework import generics
# from movie_app.models import Movie
# from .serializers import MovieSerializer


# class MovieList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer


#     def get(self, request, *args, **kwargs):
#         return self.list(*args, **kwargs)


#     def post(self, request, *args, **kwargs):
#         return self.create(*args, **kwargs)


# class MovieDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(*args, **kwargs)
