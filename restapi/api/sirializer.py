from rest_framework.serializers import ModelSerializer
from .models import Category, Article, Lvmsg

class CategorySL(ModelSerializer):
  class Meta:
    model = Category
    fields = ['cateName']

class ArticleSl(ModelSerializer):
  class Meta:
    model = Article
    fields = ['id','title','text','cate','insTime']

class LvmsgSl(ModelSerializer):
  class Meta:
    model = Lvmsg
    fields = '__all__'