from django.contrib import admin
from .models import Article,Column

# Register your models here.

class ColumnAdmin(admin.ModelAdmin):
     list_display = ('name', 'slug', 'intro',)
 
 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')
admin.site.register(Article, ArticleAdmin)

admin.site.register(Column, ColumnAdmin)
