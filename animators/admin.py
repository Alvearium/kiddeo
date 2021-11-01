from django.contrib import admin

from animators.models import Agency, Animator

# Register your models here.
@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    pass

@admin.register(Animator)
class AnimatorAdmin(admin.ModelAdmin):
    pass