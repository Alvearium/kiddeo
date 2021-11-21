# Generated by Django 3.2.9 on 2021-11-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decorations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agencydecoration',
            name='agency_description',
        ),
        migrations.RemoveField(
            model_name='agencydecoration',
            name='decoration_description',
        ),
        migrations.RemoveField(
            model_name='agencydecoration',
            name='departure_description',
        ),
        migrations.RemoveField(
            model_name='agencydecoration',
            name='requisite_description',
        ),
        migrations.RemoveField(
            model_name='agencydecoration',
            name='rules_description',
        ),
        migrations.RemoveField(
            model_name='agencydecoration',
            name='stylist_description',
        ),
        migrations.RemoveField(
            model_name='agencydecoration',
            name='time_description',
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='additionally',
            field=models.CharField(max_length=255, null=True, verbose_name='Дополнительно'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='description_1',
            field=models.TextField(null=True, verbose_name='Описание агенства'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='description_2',
            field=models.TextField(null=True, verbose_name='Описание стилистики'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='description_3',
            field=models.TextField(null=True, verbose_name='Описание рекзвиита'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='description_4',
            field=models.TextField(null=True, verbose_name='Описание выезда'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='description_5',
            field=models.TextField(null=True, verbose_name='Описание оформления'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='description_6',
            field=models.TextField(null=True, verbose_name='Описание времени'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='description_7',
            field=models.TextField(null=True, verbose_name='Описание правил'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='design_elements',
            field=models.CharField(max_length=255, null=True, verbose_name='Элементы оформления'),
        ),
        migrations.AddField(
            model_name='agencydecoration',
            name='rubric',
            field=models.CharField(max_length=255, null=True, verbose_name='Рубрика'),
        ),
        migrations.AlterField(
            model_name='agencydecoration',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Минимальная стоимость заказа'),
        ),
    ]
