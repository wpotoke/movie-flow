from rest_framework import serializers
from movie_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:

        fields = (
            "name",
            "rating",
            "rating_imdb",
            "year",
            "budget",
            "description",
            "slug",
            "currency",
            "director",
            "actor",
            "category",
            "age",
            "time",
            "updated_at",
            "image",
            "image_back",
            "video_medium",
            "video_high",
            "video_hd",
        )

        model = Movie


# class MovieSerializer(serializers.Serializer):

#     name = serializers.CharField()
#     rating = serializers.FloatField()
#     rating_imdb = serializers.FloatField()
#     year = serializers.IntegerField()
#     budget = serializers.IntegerField()
#     description = serializers.CharField()
#     slug = serializers.SlugField()
#     currency = serializers.CharField()
#     director = serializers.CharField()
#     actor = serializers.CharField()
#     category = serializers.CharField()
#     category_film = serializers.CharField()
#     age = serializers.IntegerField()
#     time = serializers.FloatField()
#     updated_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Movie(**validated_data)

#     def update(self, validated_data, instance):
#         instance.name = validated_data.get("name", instance.name)
#         instance.rating = validated_data.get("rating", instance.rating)
#         instance.rating_imdb = validated_data.get("rating_imdb", instance.rating_imdb)
#         instance.year = validated_data.get("year", instance.year)
#         instance.budget = validated_data.get("budget", instance.budget)
#         instance.description = validated_data.get("description", instance.description)
#         instance.slug = validated_data.get("slug", instance.slug)
#         instance.currency = validated_data.get("currency", instance.currency)
#         instance.director = validated_data.get("director", instance.director)
#         instance.actor = validated_data.get("actor", instance.actor)
#         instance.category = validated_data.get("category", instance.category)
#         instance.category_film = validated_data.get(
#             "category_film", instance.category_film
#         )
#         instance.age = validated_data.get("age", instance.age)
#         instance.time = validated_data.get("time", instance.time)
#         instance.updated_at = validated_data.get("updated_at", instance.updated_at)
#         return instance
