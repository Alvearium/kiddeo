# Generated by Django 3.2.9 on 2021-11-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animators', '0010_auto_20211119_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='animator',
            name='subcategory',
            field=models.CharField(max_length=255, null=True, verbose_name='Подкатегория'),
        ),
    ]