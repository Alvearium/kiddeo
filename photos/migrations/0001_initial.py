# Generated by Django 3.2.9 on 2021-12-13 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0002_auto_20211028_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('price', models.IntegerField(null=True, verbose_name='Минимальная стоимость заказа')),
                ('booking_time', models.IntegerField(verbose_name='Время брони')),
                ('price_departure', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Цена за выезд')),
                ('last_order', models.TextField(verbose_name='Последний заказ')),
                ('rubric', models.CharField(max_length=255, null=True, verbose_name='Рубрика')),
                ('types_conditions', models.CharField(max_length=255, null=True, verbose_name='Виды и условия')),
                ('result', models.CharField(max_length=255, null=True, verbose_name='Рузультат')),
                ('description_1', models.TextField(null=True, verbose_name='Описание ресторана')),
                ('description_2', models.TextField(null=True, verbose_name='Описание кухни')),
                ('description_3', models.TextField(null=True, verbose_name='Описание поваров')),
                ('description_4', models.TextField(null=True, verbose_name='Описание доставки')),
                ('description_5', models.TextField(null=True, verbose_name='Описание напитков')),
                ('description_6', models.TextField(null=True, verbose_name='Описание обслуживания')),
                ('description_7', models.TextField(null=True, verbose_name='Описание правил')),
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
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Агенство',
                'verbose_name_plural': 'Агенства',
            },
        ),
        migrations.CreateModel(
            name='AuditElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('content', models.TextField(null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Элемент аудита',
                'verbose_name_plural': 'Элементы аудитов',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=255, null=True, verbose_name='Подкатегория')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=0, max_digits=9, null=True, verbose_name='Цена без скидки')),
                ('sale', models.DecimalField(decimal_places=0, max_digits=9, null=True, verbose_name='Цена со скидкой')),
                ('mini_desc', models.CharField(max_length=255, null=True, verbose_name='Мини описание')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('duration', models.IntegerField(null=True, verbose_name='Время')),
                ('structure', models.TextField(null=True, verbose_name='Преимущества')),
                ('delivery', models.TextField(null=True, verbose_name='Доставка')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.agencyphotos', verbose_name='Агенство')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Текст')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.agencyphotos', verbose_name='Агенство')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Текст')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.agencyphotos', verbose_name='Агенство')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='ImageLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('agency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.agencyphotos', verbose_name='Агенство')),
                ('audit_element', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.auditelement', verbose_name='Элемент аудита')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.questions', verbose_name='Вопрос')),
                ('reviews', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.reviews', verbose_name='Отзывы')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Audits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('agency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.agencyphotos', verbose_name='Агенство')),
            ],
            options={
                'verbose_name': 'Аудит',
                'verbose_name_plural': 'Аудиты',
            },
        ),
        migrations.AddField(
            model_name='auditelement',
            name='audit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.audits', verbose_name='Аудит'),
        ),
    ]