from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to="user_image", blank=True, null=True, verbose_name='Аватар')
    username = models.CharField(unique=True, max_length=150, verbose_name="Имя")

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
