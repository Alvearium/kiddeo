# Generated by Django 3.0 on 2021-10-28 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premises', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='premises',
            options={'verbose_name': 'Помещение', 'verbose_name_plural': 'Помещения'},
        ),
        migrations.AlterModelOptions(
            name='premisesimage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
