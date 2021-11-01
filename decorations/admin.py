from django.contrib import admin
from decorations.models import AgencyDecoration, Decoration

@admin.register(AgencyDecoration)
class AgencyDecorationAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Рестораны'

@admin.register(Decoration)
class DecorationAdmin(admin.ModelAdmin):
    pass

