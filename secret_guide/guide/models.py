from django.db import models


class Category(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=255,
        blank=False,
        null=False,
    )

    description = models.TextField(
        'Описание',
        blank=False,
        null=False,
    )

    position = models.PositiveIntegerField(
        'Позиция на сайте',
        default=100,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.position} | {self.title}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Place(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        blank=False,
        null=False,
    )

    title = models.CharField(
        'Заголовок',
        max_length=255,
        blank=False,
        null=False,
    )

    address = models.CharField(
        'Адрес',
        max_length=255,
        blank=False,
        null=False,
    )

    map_url = models.URLField(
        'Ссылка на карту',
        max_length=255,
        blank=False,
        null=False,
    )

    photo = models.ImageField(
        'Фото',
        upload_to='guide/place',
    )

    position = models.PositiveIntegerField(
        'Позиция на сайте',
        default=100,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.category} | {self.title}"

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
