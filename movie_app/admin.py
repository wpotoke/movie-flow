from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from movie_app.models import Movie, Director, Actor, Serial


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": (
            "first_name",
            "last_name",
        )
    }


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    list_display = ["first_name", "last_name", "email", "slug"]
    list_editable = ["last_name", "email", "slug"]


class RatingFilter(admin.SimpleListFilter):

    title = "Фильтр по рейтингу"
    parameter_name = "rating"

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any]:
        if self.value() == "до 40":
            return queryset.filter(rating__lt=40)
        if self.value() == "от 40 до 59":
            return queryset.filter(rating__gt=39, rating__lt=60)
        if self.value() == "от 60 до 79":
            return queryset.filter(rating__gt=59, rating__lt=79)
        if self.value() == "от 80":
            return queryset.filter(rating__gt=79)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "rating", "currency", "budget", "rating_status", "director"]
    filter_horizontal = ["actor"]
    list_editable = ["budget", "director", "rating"]
    ordering = ["-rating", "name"]
    search_fields = ["name"]
    actions = ["set_usd", "set_rub"]
    list_filter = ["name", RatingFilter]

    @admin.display(ordering="rating")
    def rating_status(self, movie):
        if movie.rating < 50:
            return "Ужасный фильм"
        if movie.rating < 70:
            return "Средний фильм"
        if movie.rating <= 85:
            return "Хороший фильм"
        return "Прекрасный фильм"

    @admin.action(description="Поменять валюту (usd)")
    def set_usd(self, request, queryset):
        queryset.update(currency=Movie.USD)

    @admin.action(description="Поменять валюту (rub)")
    def set_rub(self, request, queryset):
        count_updated = queryset.update(currency=Movie.RUB)
        self.message_user(request, f"Обновленно {count_updated} записей")


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "rating", "currency", "budget", "category_serial"]
    filter_horizontal = ["actors"]
    list_editable = ["budget", "rating"]
    ordering = ["-rating", "name"]
    search_fields = ["name"]
    actions = ["set_usd", "set_rub"]
