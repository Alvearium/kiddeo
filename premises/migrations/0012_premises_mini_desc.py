# Generated by Django 3.2.9 on 2021-11-18 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premises', '0011_alter_premises_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='premises',
            name='mini_desc',
            field=models.CharField(max_length=255, null=True, verbose_name='Дополнительно'),
        ),
    ]
