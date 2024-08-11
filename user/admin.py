from django.contrib import admin
from .models import User

@admin.register(User)
class ActorAdmin(admin.ModelAdmin):
    ...