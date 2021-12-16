# Generated by Django 3.2.9 on 2021-12-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_auto_20211127_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='additionally',
            field=models.CharField(choices=[('Нет дополнений', 'Нет дополнений'), ('Правильное питание', 'Правильное питание'), ('Веганские блюда', 'Веганские блюда'), ('Фермерские продукты', 'Фермерские продукты'), ('Меню для малышей до 2 лет', 'Меню для малышей до 2 лет')], default='Нет дополнений', max_length=255, null=True, verbose_name='Дополнительно'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='dishes',
            field=models.CharField(choices=[('Пицца', 'Пицца'), ('Пироги', 'Пироги'), ('Бургеры и канапе', 'Бургеры и канапе'), ('Торты и десерты', 'Торты и десерты'), ('Суши и роллы', 'Суши и роллы')], default='Пицца', max_length=255, verbose_name='Блюда'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='kitchen_type',
            field=models.CharField(choices=[('Русская', 'Русская'), ('Средиземноморская', 'Средиземноморская'), ('Кавказская', 'Кавказская'), ('Восточная', 'Восточная'), ('Американская', 'Американская')], default='Русская', max_length=255, verbose_name='Тип кухни'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rubric',
            field=models.CharField(choices=[('Кейтеринг', 'Кейтеринг'), ('Доставка', 'Доставка'), ('Обслуживание', 'Обслуживание'), ('Акции %', 'Акции %')], default='Кейтеринг', max_length=255, verbose_name='Разновидность'),
        ),
    ]
