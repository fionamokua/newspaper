from xml.etree.ElementTree import Comment
from django.contrib import admin
from . import models
# Register your models here.
class CommentInLine(admin.TabularInline):
    model=models.Comment
class ArticleAdmin(admin.ModelAdmin):
    inlines=[
    CommentInLine,    ]
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Comment)