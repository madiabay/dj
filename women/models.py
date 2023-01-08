from django.db import models
from django.urls import reverse


# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})