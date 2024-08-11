from django.contrib.sitemaps import Sitemap
from .models import Movie

class MovieSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Movie.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # Предполагая, что у вас есть поле updated_at в модели Movie