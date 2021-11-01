from django.db import models
from mainapp.models import Category

# Create your models here.
class Premises(models.Model):

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length= 255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name = 'Изображения', null = True, blank = True)
    video = models.FileField(verbose_name = 'Видео')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за час')
    sale = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Скидка')
    count_peoples = models.IntegerField(verbose_name='Вместимость')
    square = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Площадь')
    floor =  models.IntegerField(verbose_name='Этаж')
    address = models.CharField(max_length = 255, verbose_name = 'Адрес')
    parking = models.BooleanField(verbose_name = 'Парковка')
    extensions = models.TextField(verbose_name = 'Дополнения')

class PremisesImage(models.Model):

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    premises = models.ForeignKey(Premises, verbose_name = 'Помещение', on_delete = models.CASCADE)
    image = models.ImageField(verbose_name = 'Изображение')