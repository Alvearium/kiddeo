# Generated by Django 3.0 on 2021-10-27 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображения')),
                ('video', models.FileField(upload_to='', verbose_name='Видео')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена за час')),
                ('sale', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Скидка')),
                ('count_peoples', models.IntegerField(verbose_name='Вместимость')),
                ('square', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Площадь')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('parking', models.BooleanField(verbose_name='Парковка')),
                ('extensions', models.TextField(verbose_name='Дополнения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='PremisesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('premises', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premises.Premises', verbose_name='Помещение')),
            ],
        ),
    ]