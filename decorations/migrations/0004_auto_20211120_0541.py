# Generated by Django 3.2.9 on 2021-11-20 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decorations', '0003_auto_20211120_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='decoration',
            name='count',
        ),
        migrations.AddField(
            model_name='decoration',
            name='durations',
            field=models.IntegerField(null=True, verbose_name='Количество'),
        ),
    ]
