# Generated by Django 3.2.9 on 2021-11-20 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animators', '0013_auto_20211119_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agency',
            old_name='duration',
            new_name='price',
        ),
    ]
