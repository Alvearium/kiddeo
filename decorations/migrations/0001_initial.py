# Generated by Django 3.0 on 2021-10-28 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0002_auto_20211028_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyDecoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('price', models.IntegerField(verbose_name='Минимальная стоимость заказа')),
                ('booking_time', models.IntegerField(verbose_name='Время брони')),
                ('price_departure', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена за выезд')),
                ('price_delivery', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Доставка')),
                ('last_order', models.TextField(verbose_name='Последний заказ')),
                ('agency_description', models.TextField(verbose_name='Описание агенства')),
                ('stylist_description', models.TextField(verbose_name='Описание стилистики')),
                ('requisite_description', models.TextField(verbose_name='Описание рекзвиита')),
                ('departure_description', models.TextField(verbose_name='Описание выезда')),
                ('decoration_description', models.TextField(verbose_name='Описание оформления')),
                ('time_description', models.TextField(verbose_name='Описание времени')),
                ('rules_description', models.TextField(verbose_name='Описание правил')),
                ('reason_1', models.TextField(verbose_name='Причина 1')),
                ('reason_2', models.TextField(verbose_name='Причина 2')),
                ('reason_3', models.TextField(verbose_name='Причина 3')),
                ('reason_4', models.TextField(verbose_name='Причина 4')),
                ('reason_5', models.TextField(verbose_name='Причина 5')),
                ('reason_6', models.TextField(verbose_name='Причина 6')),
                ('question_1', models.TextField(verbose_name='Вопрос 1')),
                ('answer_1', models.TextField(verbose_name='Ответ 1')),
                ('question_2', models.TextField(verbose_name='Вопрос 2')),
                ('answer_2', models.TextField(verbose_name='Ответ 2')),
                ('question_3', models.TextField(verbose_name='Вопрос 3')),
                ('answer_3', models.TextField(verbose_name='Ответ 3')),
                ('question_4', models.TextField(verbose_name='Вопрос 4')),
                ('answer_4', models.TextField(verbose_name='Ответ 4')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Агенство',
                'verbose_name_plural': 'Агенства',
            },
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Декорация')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('structure', models.TextField(verbose_name='Cостав')),
                ('delivery', models.TextField(verbose_name='Доставка')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decorations.AgencyDecoration', verbose_name='Агенство')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Декорация',
                'verbose_name_plural': 'Декорации',
            },
        ),
    ]
