# Generated by Django 3.2.9 on 2021-11-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animators', '0009_auto_20211119_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='subcategory',
            field=models.CharField(max_length=255, null=True, verbose_name='Подкатегория'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='price_departure',
            field=models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Цена за выезд'),
        ),
    ]