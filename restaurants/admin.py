from django.contrib import admin

from restaurants.models import Food, Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Рестораны'

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
