# Generated by Django 3.2.9 on 2021-12-15 03:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('premises', '0027_auto_20211215_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premises',
            name='count_peoples',
        ),
        migrations.AddField(
            model_name='premises',
            name='count_peoples',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('До 20 человек', 'До 20 человек'), ('От 20 до 50', 'От 20 до 50'), ('Больше 50', 'Больше 50')], default='До 20 человек', max_length=255, verbose_name='Вместимость'),
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]