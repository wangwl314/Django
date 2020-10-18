from django.contrib import admin
from .models import Category, Article, Lvmsg
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('cateName',)

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title','text','cate','insTime')
  search_fields = ['text']
admin.site.register(Article, ArticleAdmin)