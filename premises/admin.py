from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text

from premises.models import Premises, PremisesImage, Audits, AuditElement

# Register your models here.
class PremisesImageInline(admin.TabularInline):
    model = PremisesImage
    extra = 0

class AuditElementInline(admin.StackedInline):
    model = AuditElement
    extra = 0
    fields = ["get_edit_link", "title", "content"]
    readonly_fields = ["get_edit_link"]

    def get_edit_link(self, obj=None):
        if obj.pk:
            url = reverse(
                'admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),
                args=[force_text(obj.pk)]
            )
            return mark_safe("""<a href="{url}">{text}</a>""".format(
                url=url,
                text=_("Вставить изображения в %s") % obj._meta.verbose_name,
            ))
        return _("(Нажмите Сохранить и продолжить редактирование, чтобы вставить изображения)")
    get_edit_link.short_description = _("Изображения")

class AuditElementImagesInline(admin.TabularInline):
    model = PremisesImage
    fields = ["image"]
    extra = 0

@admin.register(Premises)
class PremisesAdmin(admin.ModelAdmin):
    inlines = [PremisesImageInline]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Audits)
class AuditsAdmin(admin.ModelAdmin):
    inlines = [AuditElementInline]

@admin.register(AuditElement)
class AuditElement(admin.ModelAdmin):
    inlines = [AuditElementImagesInline]

@admin.register(PremisesImage)
class PremisesImage(admin.ModelAdmin):
    pass

