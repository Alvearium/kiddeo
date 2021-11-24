from django.db import models
from mainapp.models import Category

class AgencyDecoration(models.Model):

    class Meta:
        verbose_name = 'Агенство'
        verbose_name_plural = 'Агенства'

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    rubric = models.CharField(max_length=255, verbose_name='Рубрика', null = True)
    price = models.IntegerField(verbose_name='Минимальная стоимость заказа', null = True)
    booking_time = models.IntegerField(verbose_name='Время брони')
    price_departure = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за выезд')
    price_delivery = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Доставка')
    design_elements = models.CharField(max_length=255, verbose_name='Элементы оформления', null = True)
    additionally = models.CharField(max_length= 255, verbose_name='Дополнительно', null = True)
    last_order = models.TextField(verbose_name = 'Последний заказ')
    description_1 = models.TextField(verbose_name = 'Описание агенства', null = True)
    description_2 = models.TextField(verbose_name = 'Описание стилистики', null = True)
    description_3 = models.TextField(verbose_name = 'Описание рекзвиита', null = True)
    description_4 = models.TextField(verbose_name = 'Описание выезда', null = True)
    description_5 = models.TextField(verbose_name = 'Описание оформления', null = True)
    description_6 = models.TextField(verbose_name = 'Описание времени', null = True)
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
    
class Decoration(models.Model):

    class Meta:
        verbose_name = 'Декорация'
        verbose_name_plural = 'Декорации'

    agency = models.ForeignKey(AgencyDecoration, verbose_name='Агенство', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE,)
    subcategory = models.CharField(max_length=255, verbose_name='Подкатегория', null = True)
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name = 'Изображение')
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена', null = True)
    sale = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Скидка', null = True)
    mini_description = models.CharField(max_length=255, verbose_name='Мини описание', null = True)
    description = models.TextField(verbose_name = 'Описание')
    duration = models.IntegerField(verbose_name='Количество', null = True)
    structure = models.TextField(verbose_name = 'Cостав')
    delivery = models.TextField(verbose_name = 'Доставка')


    def __str__(self):
        return self.title

class Audits(models.Model):

    class Meta:
        verbose_name = 'Аудит'
        verbose_name_plural = 'Аудиты'

    agency = models.ForeignKey(AgencyDecoration, verbose_name='Агенство', on_delete=models.CASCADE, null = True)
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

class AgencyImage(models.Model):

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    agency = models.ForeignKey(AgencyDecoration, verbose_name = 'Агенство', on_delete = models.CASCADE, null = True)
    audit_element = models.ForeignKey(AuditElement, verbose_name = 'Элемент аудита', on_delete = models.CASCADE, null = True)
    image = models.ImageField(verbose_name = 'Изображение')