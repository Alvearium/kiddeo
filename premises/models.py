from django.db import models
from django.urls.base import reverse
from mainapp.models import Category


# Create your models here.
class Premises(models.Model):

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length= 255, verbose_name='Название')
    slug = models.SlugField(unique=True,db_index=True)
    image = models.ImageField(verbose_name = 'Изображения', null = True, blank = True)
    video = models.FileField(verbose_name = 'Видео', null = True, blank = True)
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена без скидки')
    sale = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена со скидкой')
    mini_desc = models.TextField(verbose_name = 'Короткое описание', null = True)
    count_peoples = models.CharField(max_length= 255, verbose_name='Вместимость')
    square = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Площадь')
    floor =  models.IntegerField(verbose_name='Этаж')
    address = models.CharField(max_length = 255, verbose_name = 'Адрес')
    parking = models.BooleanField(verbose_name = 'Парковка')
    zoning = models.CharField(max_length= 255, verbose_name='Зонирование', null = True)
    additionally = models.CharField(max_length= 255, verbose_name='Дополнительно', null = True)
    conditions = models.CharField(max_length= 255, verbose_name='Условия', null = True)
    extensions = models.TextField(verbose_name = 'Дополнения')
    monday = models.CharField(max_length= 255, verbose_name='Понедельник', null = True)
    tuesday = models.CharField(max_length= 255, verbose_name='Вторник', null = True)
    wednesday = models.CharField(max_length= 255, verbose_name='Среда', null = True)
    thursday = models.CharField(max_length= 255, verbose_name='Четверг', null = True)
    friday = models.CharField(max_length= 255, verbose_name='Пятница', null = True)
    saturday = models.CharField(max_length= 255, verbose_name='Суббота', null = True)
    sunday = models.CharField(max_length= 255, verbose_name='Воскресенье', null = True)
    district = models.CharField(max_length= 255, verbose_name='Район', null = True)
    map_link = models.CharField(max_length= 255, verbose_name='Ссылка на картку', null = True)
    description_1 = models.TextField(verbose_name = 'Описание помещения', null = True)
    description_2 = models.TextField(verbose_name = 'Описание звукового оборудования', null = True)
    description_3 = models.TextField(verbose_name = 'Описание светового и шоу оборудования', null = True)
    description_4 = models.TextField(verbose_name = 'Описание технического оборудования', null = True)
    description_5 = models.TextField(verbose_name = 'Описание мебели', null = True)
    description_6 = models.TextField(verbose_name = 'Описание правил', null = True)
    description_7 = models.TextField(verbose_name = 'Описание кихни и посуды', null = True)
    reason_1 = models.TextField(verbose_name = 'Причина 1', null = True)
    reason_2 = models.TextField(verbose_name = 'Причина 2', null = True)
    reason_3 = models.TextField(verbose_name = 'Причина 3', null = True)
    reason_4 = models.TextField(verbose_name = 'Причина 4', null = True)
    reason_5 = models.TextField(verbose_name = 'Причина 5', null = True)
    reason_6 = models.TextField(verbose_name = 'Причина 6', null = True)
    question_1 = models.TextField(verbose_name = 'Вопрос 1', null = True)
    answer_1 = models.TextField(verbose_name = 'Ответ 1', null = True)
    question_2 = models.TextField(verbose_name = 'Вопрос 2', null = True)
    answer_2 = models.TextField(verbose_name = 'Ответ 2', null = True)
    question_3 = models.TextField(verbose_name = 'Вопрос 3', null = True)
    answer_3 = models.TextField(verbose_name = 'Ответ 3', null = True)
    question_4 = models.TextField(verbose_name = 'Вопрос 4', null = True)
    answer_4 = models.TextField(verbose_name = 'Ответ 4', null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('premise', kwargs={'premise_slug': self.slug})

class Audits(models.Model):

    class Meta:
        verbose_name = 'Аудит'
        verbose_name_plural = 'Аудиты'

    premise = models.ForeignKey(Premises, verbose_name='Помещение', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length= 255, verbose_name='Название', null = True)


    def __str__(self):
        return self.title

class AuditElement(models.Model):

    class Meta:
        verbose_name = 'Элемент аудита'
        verbose_name_plural = 'Элементы аудитов'

    audit = models.ForeignKey(Audits, verbose_name='Аудит', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length= 255, verbose_name='Название', null = True)
    content = models.TextField(verbose_name = 'Текст', null = True)

    def __str__(self):
            return self.title

class Reviews(models.Model):

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    premise = models.ForeignKey(Premises, verbose_name='Помещение', on_delete=models.CASCADE)
    title = models.CharField(max_length= 255, verbose_name='Название')
    content = models.TextField(verbose_name = 'Текст')

    def __str__(self):
        return self.title

class Questions(models.Model):

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    premise = models.ForeignKey(Premises, verbose_name='Помещение', on_delete=models.CASCADE)
    title = models.CharField(max_length= 255, verbose_name='Название')
    content = models.TextField(verbose_name = 'Текст')

    def __str__(self):
        return self.title

class ImageLibrary(models.Model):

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    premises = models.ForeignKey(Premises, verbose_name = 'Помещение', on_delete = models.CASCADE, null = True)
    reviews = models.ForeignKey(Reviews, verbose_name = 'Отзывы', on_delete = models.CASCADE, null = True)
    question =  models.ForeignKey(Questions, verbose_name = 'Вопрос', on_delete = models.CASCADE, null = True)
    audit_element = models.ForeignKey(AuditElement, verbose_name = 'Элемент аудита', on_delete = models.CASCADE, null = True)
    image = models.ImageField(verbose_name = 'Изображение')
    
