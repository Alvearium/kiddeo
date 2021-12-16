# Generated by Django 3.2.9 on 2021-12-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premises', '0024_premises_map_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premises',
            name='extensions',
        ),
        migrations.AlterField(
            model_name='premises',
            name='additionally',
            field=models.CharField(choices=[('Нет дополнений', 'Нет дополнений'), ('Оборудованная кузня', 'Оборудованная кузня'), ('Посуда', 'Посуда'), ('Музоборудование', 'Музоборудование'), ('Кондиционер', 'Кондиционер'), ('Стол для малышей', 'Стол для малышей'), ('Парковка', 'Парковка')], default='Нет дополнений', max_length=255, null=True, verbose_name='Дополнительно'),
        ),
        migrations.AlterField(
            model_name='premises',
            name='conditions',
            field=models.CharField(choices=[('Нет условий', 'Нет условий'), ('Закрывается под нас', 'Закрывается под нас'), ('Отдельный вход', 'Отдельный вход'), ('Можно со своей едой', 'Можно со своей едой'), ('Можно со своим фотогрофом/аниматором', 'Можно со своим фотогрофом/аниматором'), ('Можно украсить самим', 'Можно украсить самим'), ('Уборка после включена', 'Уборка после включена')], default='Нет условий', max_length=255, null=True, verbose_name='Условия'),
        ),
        migrations.AlterField(
            model_name='premises',
            name='count_peoples',
            field=models.CharField(choices=[('До 20 человек', 'До 20 человек'), ('От 20 до 50', 'От 20 до 50'), ('Больше 50', 'Больше 50')], default='До 20 человек', max_length=255, verbose_name='Вместимость'),
        ),
        migrations.AlterField(
            model_name='premises',
            name='district',
            field=models.CharField(choices=[('Адмиралтейский', 'Адмиралтейский'), ('Василеостровский', 'Василеостровский'), ('Выборгский', 'Выборгский'), ('Калининский', 'Калининский'), ('Кировский', 'Кировский'), ('Коллинский', 'Коллинский'), ('Красногвардейский', 'Красногвардейский'), ('Красносельский', 'Красносельский'), ('Кронштадский', 'Кронштадский')], default='Адмиралтейский', max_length=255, null=True, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='premises',
            name='square',
            field=models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='premises',
            name='zoning',
            field=models.CharField(choices=[('Нет зонирования', 'Нет зонирования'), ('Место для игр', 'Место для игр'), ('Место для переодевания', 'Место для переодевания'), ('Место для красивых фото', 'Место для красивых фото'), ('Тихий уголокдля взрослых', 'Тихий уголокдля взрослых')], default='Нет зонирования', max_length=255, null=True, verbose_name='Зонирование'),
        ),
    ]
