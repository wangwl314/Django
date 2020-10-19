from django.shortcuts import render
from .models import Article, Category
from .sirializer import ArticleSl, CategorySL
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class CategoryVS(ModelViewSet):
  serializer_class = CategorySL
  queryset = Category.objects.all()
  authentication_classes = [JWTAuthentication]

class ArticleVS(ModelViewSet):
  serializer_class = ArticleSl
  queryset = Article.objects.filter(active='yes')
  authentication_classes = [JWTAuthentication]