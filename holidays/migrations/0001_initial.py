# Generated by Django 3.2.9 on 2021-12-13 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0002_auto_20211028_0324'),
    ]

    operations = [
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
            name='Holidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображения')),
                ('video', models.FileField(blank=True, null=True, upload_to='', verbose_name='Видео')),
                ('price', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Цена без скидки')),
                ('sale', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Цена со скидкой')),
                ('count_peoples', models.CharField(max_length=255, verbose_name='Количество гостей')),
                ('time', models.IntegerField(verbose_name='Время праздника')),
                ('premise', models.BooleanField(verbose_name='Помещение включено')),
                ('square', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Площадь помещения')),
                ('entertainment', models.BooleanField(verbose_name='Развлечения включены')),
                ('entertainment_type', models.CharField(max_length=255, null=True, verbose_name='Развлечение')),
                ('food', models.BooleanField(verbose_name='Кормить будем')),
                ('food_type', models.CharField(max_length=255, null=True, verbose_name='Еда')),
                ('shooting', models.BooleanField(verbose_name='Съёмка включена')),
                ('shooting_type', models.CharField(max_length=255, null=True, verbose_name='Вид съёмки')),
                ('shooting_time', models.CharField(max_length=255, null=True, verbose_name='Время съёмки')),
                ('decoration', models.BooleanField(verbose_name='Оформление включено')),
                ('decoration_type', models.CharField(max_length=255, null=True, verbose_name='Оформление')),
                ('mini_desc', models.TextField(null=True, verbose_name='Короткое описание')),
                ('guests_gender', models.CharField(max_length=255, null=True, verbose_name='Пол гостей')),
                ('guests_age', models.CharField(max_length=255, null=True, verbose_name='Возраст гостей')),
                ('monday', models.CharField(max_length=255, null=True, verbose_name='Понедельник')),
                ('tuesday', models.CharField(max_length=255, null=True, verbose_name='Вторник')),
                ('wednesday', models.CharField(max_length=255, null=True, verbose_name='Среда')),
                ('thursday', models.CharField(max_length=255, null=True, verbose_name='Четверг')),
                ('friday', models.CharField(max_length=255, null=True, verbose_name='Пятница')),
                ('saturday', models.CharField(max_length=255, null=True, verbose_name='Суббота')),
                ('sunday', models.CharField(max_length=255, null=True, verbose_name='Воскресенье')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('map_link', models.CharField(max_length=255, null=True, verbose_name='Ссылка на картку')),
                ('description_1', models.TextField(null=True, verbose_name='Описание помещения')),
                ('description_2', models.TextField(null=True, verbose_name='Описание звукового оборудования')),
                ('description_3', models.TextField(null=True, verbose_name='Описание светового и шоу оборудования')),
                ('description_4', models.TextField(null=True, verbose_name='Описание технического оборудования')),
                ('description_5', models.TextField(null=True, verbose_name='Описание мебели')),
                ('description_6', models.TextField(null=True, verbose_name='Описание правил')),
                ('description_7', models.TextField(null=True, verbose_name='Описание кихни и посуды')),
                ('reason_1', models.TextField(null=True, verbose_name='Причина 1')),
                ('reason_2', models.TextField(null=True, verbose_name='Причина 2')),
                ('reason_3', models.TextField(null=True, verbose_name='Причина 3')),
                ('reason_4', models.TextField(null=True, verbose_name='Причина 4')),
                ('reason_5', models.TextField(null=True, verbose_name='Причина 5')),
                ('reason_6', models.TextField(null=True, verbose_name='Причина 6')),
                ('question_1', models.TextField(null=True, verbose_name='Вопрос 1')),
                ('answer_1', models.TextField(null=True, verbose_name='Ответ 1')),
                ('question_2', models.TextField(null=True, verbose_name='Вопрос 2')),
                ('answer_2', models.TextField(null=True, verbose_name='Ответ 2')),
                ('question_3', models.TextField(null=True, verbose_name='Вопрос 3')),
                ('answer_3', models.TextField(null=True, verbose_name='Ответ 3')),
                ('question_4', models.TextField(null=True, verbose_name='Вопрос 4')),
                ('answer_4', models.TextField(null=True, verbose_name='Ответ 4')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Готовый праздник',
                'verbose_name_plural': 'Готовые праздники',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Текст')),
                ('holiday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holidays.holidays', verbose_name='Праздник')),
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
                ('holiday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holidays.holidays', verbose_name='Праздник')),
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
                ('audit_element', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='holidays.auditelement', verbose_name='Элемент аудита')),
                ('holiday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='holidays.holidays', verbose_name='Праздник')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='holidays.questions', verbose_name='Вопрос')),
                ('reviews', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='holidays.reviews', verbose_name='Отзывы')),
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
                ('holiday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='holidays.holidays', verbose_name='Праздник')),
            ],
            options={
                'verbose_name': 'Аудит',
                'verbose_name_plural': 'Аудиты',
            },
        ),
        migrations.AddField(
            model_name='auditelement',
            name='audit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='holidays.audits', verbose_name='Аудит'),
        ),
    ]