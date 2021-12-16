from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateField, SlugField, TextField
from django.db.models.fields.related import ForeignKey
from mdeditor.fields import MDTextField
from django.forms import ModelForm


# Create your models here.

class Rubrics(models.Model):
   class Meta:
        verbose_name = 'Рубрика статьи'
        verbose_name_plural = 'Рубрики статей' 

   title = models.CharField(max_length=255, verbose_name='Имя категории')
   slug = models.SlugField(unique=True)

   def __str__(self):
            return self.title
    
class Blog(models.Model):
    class Meta:
        verbose_name = 'Cтатью'
        verbose_name_plural = 'Статьи' 

    rubric = ForeignKey(Rubrics, verbose_name='Рубрика', on_delete=models.CASCADE, null = True)
    title = CharField(max_length = 255, verbose_name = "Название")
    slug = models.SlugField(unique=True, db_index=True, null=True)
    mini_desc = TextField(max_length = 255, verbose_name = "Мини описание")
    image = models.ImageField(verbose_name = "Изобажение", null = True)
    status = models.BooleanField(verbose_name = "Не публиковать")
    content = MDTextField(verbose_name = "Контент", null = True)
    date = models.DateField(verbose_name = "Дата статьи", null = True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии' 

    status = BooleanField(verbose_name = "Прошел модерацию")
    title_post = ForeignKey(Blog, verbose_name = "Название статьи", on_delete=models.CASCADE, null = True)
    name = CharField(max_length = 255, verbose_name = "Имя пользователя")
    content = TextField(verbose_name = "Комментарий")
    date = DateField(verbose_name = "", null = True)

    def __str__(self):
        return self.name