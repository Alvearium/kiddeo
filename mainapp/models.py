from django.db import models
from django.db.models.fields import related

class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

#class Cart(models.Model):

#    cart - object
#        {
#            count
#            price
#            sale
#            result_price
#        }
#   products- object
#        {
#           id
#           image
#           link
#           title
#           address
#           price
#           sale
 #          count
 #       }