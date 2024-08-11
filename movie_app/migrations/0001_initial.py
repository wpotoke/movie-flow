# Generated by Django 4.2.9 on 2024-07-03 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('gender', models.CharField(choices=[('M', 'мужчина'), ('F', 'женщина')], default='M', max_length=1, verbose_name='Гендер')),
                ('image', models.ImageField(blank=True, default='static/images/not_image.jpeg', null=True, upload_to='static/images/actors')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, verbose_name='URL')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Возвраст')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место рождения')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Биография')),
            ],
            options={
                'verbose_name': 'Актера',
                'verbose_name_plural': 'Актеры',
                'db_table': 'actor',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Режисер',
                'verbose_name_plural': 'Режисеры',
                'db_table': 'derictor',
            },
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('rating', models.FloatField(blank=True, null=True, verbose_name='Рейтинг')),
                ('rating_imdb', models.FloatField(blank=True, null=True, verbose_name='Рейтинг IMDb')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('budget', models.IntegerField(default=100000, verbose_name='Бюджет')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(default='', max_length=200, unique=True, verbose_name='URL')),
                ('currency', models.CharField(choices=[('EUR', 'Euro'), ('RUB', 'Ruble'), ('PND', 'Pound'), ('USD', 'Dollar')], default='USD', max_length=3, verbose_name='Валюта')),
                ('category_serial', models.CharField(blank=True, choices=[('NEWRELEASES', 'new_releases'), ('POPULAR', 'popular'), ('CLASSICS', 'classics'), ('COMMON', 'common')], default='COMMON', max_length=100, null=True, verbose_name='Категория сериала')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Возрастное ограничение')),
                ('time', models.FloatField(blank=True, null=True, verbose_name='Время просмотра')),
                ('image', models.ImageField(blank=True, null=True, upload_to='serials', verbose_name='Изображение')),
                ('image_back', models.ImageField(blank=True, null=True, upload_to='serial_back', verbose_name='Фон')),
                ('actors', models.ManyToManyField(related_name='serials', to='movie_app.actor', verbose_name='Актеры')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='serials', to='movie_app.director', verbose_name='Режиссер')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
                'db_table': 'serial',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('rating', models.FloatField(blank=True, null=True, verbose_name='Рейтинг')),
                ('rating_imdb', models.FloatField(blank=True, null=True, verbose_name='Рейтинг IMDb')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('budget', models.IntegerField(default=100000, verbose_name='Бюджет')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(default='', max_length=200, unique=True, verbose_name='URL')),
                ('currency', models.CharField(choices=[('EUR', 'Euro'), ('RUB', 'Ruble'), ('PND', 'Pound'), ('USD', 'Dollar')], default='USD', max_length=3)),
                ('category', models.CharField(choices=[('NEWRELEASES', 'new_releases'), ('POPULAR', 'popular'), ('CLASSICS', 'classics'), ('COMMON', 'common')], default='COMMON', max_length=50, verbose_name='Категория для главной')),
                ('category_film', models.CharField(blank=True, max_length=100, null=True, verbose_name='Категория фильма')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Возврастное ограничение')),
                ('time', models.FloatField(blank=True, null=True, verbose_name='Время просмотра')),
                ('image', models.ImageField(blank=True, null=True, upload_to='movies', verbose_name='Изображение')),
                ('image_back', models.ImageField(blank=True, null=True, upload_to='movies_back', verbose_name='Фон')),
                ('video_medium', models.FileField(blank=True, null=True, upload_to='videos/480', verbose_name='Видео 480')),
                ('video_high', models.FileField(blank=True, null=True, upload_to='videos/720', verbose_name='Видео 720')),
                ('video_hd', models.FileField(blank=True, null=True, upload_to='videos/1080', verbose_name='Видео 1080')),
                ('actor', models.ManyToManyField(related_name='movies', to='movie_app.actor', verbose_name='Актер')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='movie_app.director', verbose_name='Режисер')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', max_length=200, unique=True, verbose_name='URL')),
                ('season_number', models.PositiveIntegerField(verbose_name='Номер сезона')),
                ('episode_number', models.PositiveIntegerField(verbose_name='Номер серии')),
                ('name', models.CharField(max_length=100, verbose_name='Название серии')),
                ('image', models.ImageField(blank=True, null=True, upload_to='episodes', verbose_name='Изображение')),
                ('video_medium', models.FileField(blank=True, null=True, upload_to='videos/serials/480', verbose_name='Видео 480p')),
                ('video_high', models.FileField(blank=True, null=True, upload_to='videos/serials/720', verbose_name='Видео 720p')),
                ('video_hd', models.FileField(blank=True, null=True, upload_to='videos/serials/1080', verbose_name='Видео 1080p')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='movie_app.serial', verbose_name='Сериал')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
                'db_table': 'episode',
                'unique_together': {('serial', 'season_number', 'episode_number')},
            },
        ),
    ]
