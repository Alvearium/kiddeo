# Generated by Django 3.2.9 on 2021-11-18 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premises', '0012_premises_mini_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premises',
            name='mini_desc',
            field=models.TextField(null=True, verbose_name='Короткое описание'),
        ),
    ]
