from django.db import models
from mainapp.models import Category

class Restaurant(models.Model):

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Минимальная стоимость')
    booking_time = models.IntegerField(verbose_name='Время брони')
    price_delivery = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена доставка')
    last_order = models.TextField(verbose_name = 'Последний заказ')
    main_description = models.TextField(verbose_name = 'Описание ресторана')
    kitchen_description = models.TextField(verbose_name = 'Описание кухни')
    cooks_description = models.TextField(verbose_name = 'Описание поваров')
    delivery_description = models.TextField(verbose_name = 'Описание доставки')
    drinks_description = models.TextField(verbose_name = 'Описание напитков')
    servic_description = models.TextField(verbose_name = 'Описание обслуживания')
    rules_description = models.TextField(verbose_name = 'Описание правил')
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
    name = models.CharField(max_length=255, verbose_name='Название блюда')
    image = models.ImageField(verbose_name = 'Изображение')
    description = models.TextField(verbose_name = 'Описание')
    # category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE,)
    count_peoples = models.IntegerField(verbose_name='Количество людей')
    structure = models.TextField(verbose_name = 'Cостав')
    delivery = models.TextField(verbose_name = 'Доставка')

    def __str__(self):
        return self.name
