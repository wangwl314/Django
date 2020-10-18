from rest_framework.serializers import ModelSerializer
from .models import Category, Article

class CategorySL(ModelSerializer):
  class Meta:
    model = Category
    fields = ['cateName']

class ArticleSl(ModelSerializer):
  class Meta:
    model = Article
    fields = ['title','text','cate','insTime']