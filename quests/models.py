from django.db import models

# Create your models here.


class IconsWhy(models.Model):
    header = models.CharField('Заголовок', max_length=255)
    description = models.CharField('Описание', max_length=255)
    file = models.FileField('Иконка', upload_to='icons_why')

    def __str__(self) -> str:
        return f'{self.header}, {self.description[:10]}...'

    class Meta:
        verbose_name = 'Иконка почему'
        verbose_name_plural = 'Иконки почему'


class IconsWhen(models.Model):
    header = models.CharField('Заголовок', max_length=255)
    description = models.CharField('Описание', max_length=255)
    file = models.FileField('Иконка', upload_to='icons_when')

    def __str__(self) -> str:
        return f'{self.header}, {self.description[:10]}...'

    class Meta:
        verbose_name = 'Иконка когда'
        verbose_name_plural = 'Иконки когда'


class Photo(models.Model):
    name = models.CharField('Название фото', max_length=255)
    file = models.FileField('Файл с фото', upload_to='photo')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Video(models.Model):
    name = models.CharField('Название видео', max_length=255)
    file = models.FileField('Файл с видео', upload_to='video')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Review(models.Model):
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Отзыв')
    photo = models.FileField('Фото', upload_to='reviews')

    def __str__(self) -> str:
        return f"{self.name}, {self.text[:20]}..."

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Quest(models.Model):
    name = models.CharField('Название квеста англ', max_length=255)
    name_rus = models.CharField('Название квеста рус', max_length=255)
    description = models.CharField('Описание квеста', max_length=255)
    price = models.PositiveIntegerField('Цена')
    what_waits_you = models.TextField('Что вас ждет')
    why_it_need = models.ManyToManyField(
        IconsWhy,
        verbose_name='Иконки почему'
    )
    when_it_need = models.ManyToManyField(
        IconsWhen,
        verbose_name='Иконки когда'
    )
    photo = models.ManyToManyField(
        Photo,
        verbose_name='Фото'
    )
    video = models.ManyToManyField(
        Video,
        verbose_name='Видео'
    )
    reviews = models.ManyToManyField(
        Review,
        verbose_name='Отзывы'
    )

    def what_waits_you_list(self):
        return self.what_waits_you.replace('$$$', f'{self.price}').split('\n')

    def get_why_it_need(self):
        return "\n".join([str(p) for p in self.why_it_need.all()])

    def get_when_it_need(self):
        return "\n".join([str(p) for p in self.when_it_need.all()])

    def get_photo(self):
        return "\n".join([str(p) for p in self.photo.all()])

    def get_video(self):
        return "\n".join([str(p) for p in self.video.all()])

    def get_reviews(self):
        return "\n".join([str(p) for p in self.reviews.all()])

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Квест'
        verbose_name_plural = 'Квесты'
