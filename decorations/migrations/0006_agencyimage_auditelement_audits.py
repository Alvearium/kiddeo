# Generated by Django 3.0 on 2021-11-23 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decorations', '0005_rename_durations_decoration_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('agency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='decorations.AgencyDecoration', verbose_name='Агенство')),
            ],
            options={
                'verbose_name': 'Аудит',
                'verbose_name_plural': 'Аудиты',
            },
        ),
        migrations.CreateModel(
            name='AuditElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('content', models.TextField(null=True, verbose_name='Текст')),
                ('audit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='decorations.Audits', verbose_name='Аудит')),
            ],
            options={
                'verbose_name': 'Элемент аудита',
                'verbose_name_plural': 'Элементы аудитов',
            },
        ),
        migrations.CreateModel(
            name='AgencyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('agency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='decorations.AgencyDecoration', verbose_name='Агенство')),
                ('audit_element', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='decorations.AuditElement', verbose_name='Элемент аудита')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]