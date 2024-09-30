from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    content = models.TextField(blank=True)
    category = models.ForeignKey('Category', default='Разное', on_delete=models.SET_DEFAULT)
    tags = models.ManyToManyField('Tag', blank=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class Tag(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    text = models.TextField('Поделитесь своим мнением по теме статьи')
    created = models.DateTimeField('Добавлен', auto_now_add=True)
    moder = models.BooleanField(default=True)