# Generated by Django 3.2.9 on 2021-11-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_alter_food_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Текст')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant', verbose_name='Ресторан')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Текст')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant', verbose_name='Ресторан')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='restaurantimage',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.questions', verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='restaurantimage',
            name='reviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.reviews', verbose_name='Отзывы'),
        ),
    ]
