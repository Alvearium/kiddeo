# Generated by Django 3.2.9 on 2021-11-20 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decorations', '0004_auto_20211120_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='decoration',
            old_name='durations',
            new_name='duration',
        ),
    ]
