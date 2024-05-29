from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Почта")
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name="URL")

    class Meta:
        db_table = "derictor"
        verbose_name = "Режисер"
        verbose_name_plural = "Режисеры"

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Actor(models.Model):

    MALE = "M"
    FEMALE = "F"

    GENDERS = [
        (MALE, "мужчина"),
        (FEMALE, "женщина")
    ]

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE, verbose_name="Гендер")
    image = models.ImageField(upload_to="static/images/actors", blank=True, null=True, default="static/images/not_image.jpeg",)
    slug = models.SlugField(max_length=100, blank=True, null=True, verbose_name="URL")
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name="Возвраст")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Место рождения")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Биография")

    class Meta:
        db_table = "actor"
        verbose_name = "Актера"
        verbose_name_plural = "Актеры"

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актер {self.first_name} {self.last_name}"
        return f"Актриса {self.first_name} {self.last_name}"


class Movie(models.Model):

    EURO = "EUR"
    RUB = "RUB"
    POUND = "PND"
    USD = "USD"

    CURRENCY_CHOICES = [
        (EURO, "Euro"),
        (RUB, "Ruble"),
        (POUND, "Pound"),
        (USD, "Dollar"),
    ]

    NEWRELEASES = "NEWRELEASES"
    POPULAR = "POPULAR"
    CLASSICS = "CLASSICS"
    COMMON = "COMMON"

    CATEGORY_CHOICES = [
        (NEWRELEASES, "new_releases"),
        (POPULAR, "popular"),
        (CLASSICS, "classics"),
        (COMMON, "common"),
    ]

    name = models.CharField(max_length=40, verbose_name="Название")
    rating = models.FloatField(null=True, blank=True, verbose_name="Рейтинг")
    rating_imdb = models.FloatField(null=True, blank=True, verbose_name="Рейтинг IMDb")
    year = models.IntegerField(null=True, blank=True, verbose_name="Год")
    budget = models.IntegerField(default=100000, verbose_name="Бюджет")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    slug = models.SlugField(default="", max_length=200, unique=True, null=False, verbose_name="URL")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, blank=True, null=True, related_name="movies", verbose_name="Режисер")
    actor = models.ManyToManyField(Actor, related_name="movies", verbose_name="Актер")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=COMMON, verbose_name="Категория для главной")
    category_film = models.CharField(max_length=100, unique=False, blank=True, null=True, verbose_name="Категория фильма")
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name="Возврастное ограничение")
    time = models.FloatField(blank=True, null=True, verbose_name="Время просмотра")
    image = models.ImageField(upload_to="movies", blank=True, null=True, verbose_name="Изображение")
    image_back = models.ImageField(upload_to="movies_back", blank=True, null=True, verbose_name="Фон")
    video = models.FileField(upload_to="videos", blank=True, null=True, verbose_name="Видео")
    

    class Meta:
        db_table = "movie"
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return f"{self.name} - {self.rating}%"
