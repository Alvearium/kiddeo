# Generated by Django 3.0 on 2021-11-26 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animators', '0020_auto_20211126_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animator',
            old_name='mini_description',
            new_name='mini_desc',
        ),
    ]