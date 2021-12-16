# Generated by Django 3.0 on 2021-12-11 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='title_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='Название статьи'),
        ),
    ]
