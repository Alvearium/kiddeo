from django.contrib import admin
from django.contrib.admin.options import TabularInline

from blog.models import Blog, Comments, Rubrics

# Register your models here.
@admin.register(Rubrics)
class RubricAdmin(admin.ModelAdmin):
    pass

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
   pass

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]