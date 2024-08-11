from django.contrib import admin
from movie_app.models import Episode

@admin.register(Episode)
class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}