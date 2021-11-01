from django.contrib import admin
from django.db import models

from premises.models import Premises, PremisesImage

# Register your models here.
class PremisesImageInline(admin.TabularInline):
    model = PremisesImage
    extra = 0

@admin.register(Premises)
class PremisesAdmin(admin.ModelAdmin):
    inlines = [PremisesImageInline]

@admin.register(PremisesImage)
class PremisesImage(admin.ModelAdmin):
    pass