from django.db import models
from django.urls import reverse


# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=200, verbose_name='Титулка')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обнова')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', related_name='women')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женшины'
        verbose_name_plural = 'Известные женшины'
        ordering = ('id',)

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'