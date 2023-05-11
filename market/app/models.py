from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE = (
    ('seller', 'Продавец'),
    ('buyer', 'Покупатель'),
)


class User(AbstractUser):
    """Переопределяем модель User."""

    role = models.CharField(
        verbose_name='Пользовательская роль',
        max_length=16,
        choices=ROLE,
        blank=True,
        help_text='Выберите пользовательскую роль'
    )


class Lot(models.Model):
    """Лоты."""

    pass


class Review(models.Model):
    """Отзывы."""

    pass


class Deal(models.Model):
    """Сделки."""

    pass
