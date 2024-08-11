from django.db import models
from django.urls import reverse

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
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    image = models.ImageField(upload_to="movies", blank=True, null=True, verbose_name="Изображение")
    image_back = models.ImageField(upload_to="movies_back", blank=True, null=True, verbose_name="Фон")
    video_medium = models.FileField(upload_to='videos/480', blank=True, null=True, verbose_name="Видео 480")
    video_high = models.FileField(upload_to='videos/720', blank=True, null=True, verbose_name="Видео 720")
    video_hd = models.FileField(upload_to='videos/1080', blank=True, null=True, verbose_name="Видео 1080")

    class Meta:
        db_table = "movie"
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return f"{self.name} - {self.rating}"

    def get_video_sources(self):
        sources = []
        if self.video_medium:
            sources.append('480p')
        if self.video_high:
            sources.append('720p')
        if self.video_hd:
            sources.append('1080p')
        return sources
    
    def get_absolute_url(self):
        return reverse('index:movie-detail',
                       args=[self.slug])

class Serial(models.Model):
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

    name = models.CharField(max_length=40, verbose_name="Название")
    rating = models.FloatField(null=True, blank=True, verbose_name="Рейтинг")
    rating_imdb = models.FloatField(null=True, blank=True, verbose_name="Рейтинг IMDb")
    year = models.IntegerField(null=True, blank=True, verbose_name="Год")
    budget = models.IntegerField(default=100000, verbose_name="Бюджет")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    slug = models.SlugField(default="", max_length=200, unique=True, null=False, verbose_name="URL")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD, verbose_name="Валюта")
    director = models.ForeignKey('Director', on_delete=models.PROTECT, blank=True, null=True, related_name="serials", verbose_name="Режиссер")
    actors = models.ManyToManyField('Actor', related_name="serials", verbose_name="Актеры")
    category_serial = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=COMMON, blank=True, null=True, verbose_name="Категория сериала")
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name="Возрастное ограничение")
    time = models.FloatField(blank=True, null=True, verbose_name="Время просмотра")
    image = models.ImageField(upload_to="serials", blank=True, null=True, verbose_name="Изображение")
    image_back = models.ImageField(upload_to="serial_back", blank=True, null=True, verbose_name="Фон")

    class Meta:
        db_table = "serial"
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"

    def __str__(self):
        return f"{self.name} - {self.rating}"
    
class Episode(models.Model):
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE, related_name='episodes', verbose_name="Сериал")
    slug = models.SlugField(default="", max_length=200, unique=True, null=False, verbose_name="URL")
    season_number = models.PositiveIntegerField(verbose_name="Номер сезона")
    episode_number = models.PositiveIntegerField(verbose_name="Номер серии")
    name = models.CharField(max_length=100, verbose_name="Название серии")
    image = models.ImageField(upload_to="episodes", blank=True, null=True, verbose_name="Изображение")
    video_medium = models.FileField(upload_to='videos/serials/480', blank=True, null=True, verbose_name="Видео 480p")
    video_high = models.FileField(upload_to='videos/serials/720', blank=True, null=True, verbose_name="Видео 720p")
    video_hd = models.FileField(upload_to='videos/serials/1080', blank=True, null=True, verbose_name="Видео 1080p")

    class Meta:
        db_table = "episode"
        verbose_name = "Серия"
        verbose_name_plural = "Серии"
        unique_together = ['serial', 'season_number', 'episode_number']

    def __str__(self):
        return f"Сериал: {self.serial.name}, Сезон: {self.season_number}, Серия: {self.episode_number}"

    def get_video_sources(self):
        sources = []
        if self.video_medium:
            sources.append('480p')
        if self.video_high:
            sources.append('720p')
        if self.video_hd:
            sources.append('1080p')
        return sources
