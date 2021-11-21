# Generated by Django 3.2.9 on 2021-11-19 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animators', '0006_alter_animator_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animator',
            name='title',
        ),
        migrations.AddField(
            model_name='animator',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='animators.agency', verbose_name='Агенство'),
        ),
    ]
