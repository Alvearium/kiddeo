# Generated by Django 3.2.9 on 2021-12-15 03:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premises', '0025_auto_20211213_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('1', 'one')], default='1', max_length=2), size=None)),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
    ]
