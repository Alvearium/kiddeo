from django.db import models
from mainapp.models import Category

class Restaurant(models.Model):

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    rubric = models.CharField(max_length=255, verbose_name='Рубрика', null = True)
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Минимальная стоимость')
    booking_time = models.IntegerField(verbose_name='Время брони')
    price_departure = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена за доставку', null = True)
    last_order = models.TextField(verbose_name = 'Последний заказ')
    service = models.BooleanField(verbose_name = 'Обслуживание', null = True)
    dishes = models.CharField(max_length=255, verbose_name='Блюда', null = True)
    kitchen_type = models.CharField(max_length=255, verbose_name='Тип кухни', null = True)
    additionally = models.CharField(max_length= 255, verbose_name='Дополнительно', null = True)
    description_1 = models.TextField(verbose_name = 'Описание ресторана', null = True)
    description_2 = models.TextField(verbose_name = 'Описание кухни', null = True)
    description_3 = models.TextField(verbose_name = 'Описание поваров', null = True)
    description_4 = models.TextField(verbose_name = 'Описание доставки', null = True)
    description_5 = models.TextField(verbose_name = 'Описание напитков', null = True)
    description_6 = models.TextField(verbose_name = 'Описание обслуживания', null = True)
    description_7 = models.TextField(verbose_name = 'Описание правил', null = True)
    reason_1 = models.TextField(verbose_name = 'Причина 1')
    reason_2 = models.TextField(verbose_name = 'Причина 2')
    reason_3 = models.TextField(verbose_name = 'Причина 3')
    reason_4 = models.TextField(verbose_name = 'Причина 4')
    reason_5 = models.TextField(verbose_name = 'Причина 5')
    reason_6 = models.TextField(verbose_name = 'Причина 6')
    question_1 = models.TextField(verbose_name = 'Вопрос 1')
    answer_1 = models.TextField(verbose_name = 'Ответ 1')
    question_2 = models.TextField(verbose_name = 'Вопрос 2')
    answer_2 = models.TextField(verbose_name = 'Ответ 2')
    question_3 = models.TextField(verbose_name = 'Вопрос 3')
    answer_3 = models.TextField(verbose_name = 'Ответ 3')
    question_4 = models.TextField(verbose_name = 'Вопрос 4')
    answer_4 = models.TextField(verbose_name = 'Ответ 4')

    def __str__(self):
        return self.title
    

class Food(models.Model):

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда' 

    restaurant = models.ForeignKey(Restaurant, verbose_name='Ресторан', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null = True)
    subcategory = models.CharField(max_length=255, verbose_name='Подкатегория', null = True)
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name = 'Изображение')
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена без скидки', null = True)
    sale = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена со скидкой', null = True)
    mini_desc = models.CharField(max_length=255, verbose_name='Мини описание', null = True)
    description = models.TextField(verbose_name = 'Описание', null = True)
    duration = models.IntegerField(verbose_name='Масса', null = True)
    structure = models.TextField(verbose_name = 'Cостав', null = True)
    delivery = models.TextField(verbose_name = 'Доставка', null = True)

    def __str__(self):
        return self.title

class Audits(models.Model):

    class Meta:
        verbose_name = 'Аудит'
        verbose_name_plural = 'Аудиты'

    agency = models.ForeignKey(Restaurant, verbose_name='Ресторан', on_delete=models.CASCADE, null = True)
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

    restaurant = models.ForeignKey(Restaurant, verbose_name='Ресторан', on_delete=models.CASCADE)
    title = models.CharField(max_length= 255, verbose_name='Название')
    content = models.TextField(verbose_name = 'Текст')

    def __str__(self):
        return self.title

class Questions(models.Model):

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    restaurant = models.ForeignKey(Restaurant, verbose_name='Ресторан', on_delete=models.CASCADE)
    title = models.CharField(max_length= 255, verbose_name='Название')
    content = models.TextField(verbose_name = 'Текст')

    def __str__(self):
        return self.title


class ImageLibrary(models.Model):

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    agency = models.ForeignKey(Restaurant, verbose_name = 'Ресторан', on_delete = models.CASCADE, null = True)
    reviews = models.ForeignKey(Reviews, verbose_name = 'Отзывы', on_delete = models.CASCADE, null = True)
    question =  models.ForeignKey(Questions, verbose_name = 'Вопрос', on_delete = models.CASCADE, null = True)
    audit_element = models.ForeignKey(AuditElement, verbose_name = 'Элемент аудита', on_delete = models.CASCADE, null = True)
    image = models.ImageField(verbose_name = 'Изображение')