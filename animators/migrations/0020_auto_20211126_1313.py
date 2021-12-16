# Generated by Django 3.2.9 on 2021-11-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animators', '0019_auto_20211125_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animator',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=9, null=True, verbose_name='Цена без скидки'),
        ),
        migrations.AlterField(
            model_name='animator',
            name='sale',
            field=models.DecimalField(decimal_places=0, max_digits=9, null=True, verbose_name='Цена со скидкой'),
        ),
    ]