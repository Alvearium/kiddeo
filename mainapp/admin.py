from django.contrib import admin

from mainapp.models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass