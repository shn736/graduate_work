from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(max_length=35, verbose_name="Телефон", null=True)
    country = models.CharField(max_length=50, verbose_name="Страна", null=True)
    tg_nick = models.CharField(max_length=50, verbose_name="Телеграм ник", null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
