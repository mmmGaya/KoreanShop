from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Goods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Описание товара')
    cost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория' )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('good', kwargs={'good_slug': self.slug})
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"
        ordering = ['cost']


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, null=True, verbose_name='Номер телефона')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, verbose_name='Фото')


    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = "Покупатели"

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.id})
    


     



