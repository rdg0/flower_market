from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE = (
    ('seller', 'Продавец'),
    ('buyer', 'Покупатель'),
)
TONE = (
    ('red', 'красный'),
    ('green', 'зеленный'),
    ('blue', 'синий'),
)


class User(AbstractUser):
    """Переопределяем модель User."""

    role = models.CharField(
        verbose_name='Пользовательская роль',
        max_length=32,
        choices=ROLE,
        help_text='Выберите пользовательскую роль',
    )


class Lot(models.Model):
    """Лоты."""

    kind = models.CharField(
        verbose_name='Сорт цветка',
        max_length=256,
        db_index=True,
        help_text='Обязательное поле. Введите вид цветка',
    )
    tone = models.CharField(
        verbose_name='Оттенок',
        max_length=32,
        choices=TONE,
        help_text='Выберите оттенок цветка',
    )
    price = models.IntegerField(
        verbose_name='Цена',
        help_text='Укажите цену лота',
    )
    quantity = models.IntegerField(
        verbose_name='Количество',
        help_text='Укажите количество лота',
    )
    is_published = models.BooleanField(
        verbose_name='Опубликован ли лот',
        help_text='Выберете статус публикации лота',
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lots',
        verbose_name='Продавец лота',
        help_text='Продавец лота',
    )

    class Meta:
        ordering = ['price']
        verbose_name = 'Лот продавца'
        verbose_name_plural = 'Лоты продавцов'


class ReviewLot(models.Model):
    """Отзывы к лотам."""

    lot = models.ForeignKey(
        Lot,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Отзыв к лоту',
        help_text='Отзыв к лоту',
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text='Введите текст отзыва.',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Отзыв покупателя',
        help_text='Отзыв покупателя',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Отзыв к лоту'
        verbose_name_plural = 'Отзывы к лотам'


class ReviewSeller(models.Model):
    """Отзывы на продавцов."""

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Отзыв на продавца',
        help_text='Отзыв на продавца',
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text='Введите текст отзыва.',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Отзыв покупателя',
        help_text='Отзыв покупателя',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Отзыв на продавца'
        verbose_name_plural = 'Отзывы на продавцов'


class Deal(models.Model):
    """Сделки."""
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sellers',
        verbose_name='Продавец',
        help_text='Продавец',
    )
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buyers',
        verbose_name='Покупатель',
        help_text='Покупатель',
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'


class DealItem(models.Model):
    """Содержимое сделки."""
    deal = models.ForeignKey(
        Deal,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='Сделка',
        help_text='Сделка',
    )
    lot = models.ForeignKey(
        Lot,
        on_delete=models.CASCADE,
        related_name='lots',
        verbose_name='Лот',
        help_text='Лот',
    )
    price = models.IntegerField(
        verbose_name='Цена',
        help_text='Укажите цену сделки',
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name='Количество товара',
        help_text='Введите количество',
    )

    class Meta:
        verbose_name = 'Содержимое сделки'
        verbose_name_plural = 'Содержимое сделки'



# Ниже модели не связные с вышестоящими. Для проверки задания с собеса


class City(models.Model):
    name = models.CharField(max_length=256)


class Person(models.Model):
    name = models.CharField(max_length=256)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='cities',
    )
