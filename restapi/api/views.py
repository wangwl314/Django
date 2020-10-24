from django.shortcuts import render
from .models import Article, Category, Lvmsg
from .sirializer import ArticleSl, CategorySL, LvmsgSl
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class CategoryVS(ModelViewSet):
  serializer_class = CategorySL
  queryset = Category.objects.all()
  authentication_classes = [JWTAuthentication]
  throttle_classes = [AnonRateThrottle]
  permission_classes = [IsAuthenticatedOrReadOnly]

class ArticleVS(ModelViewSet):
  queryset = Article.objects.filter(active='yes')
  serializer_class = ArticleSl
  throttle_classes = [AnonRateThrottle]
  permission_classes = [IsAuthenticatedOrReadOnly]
  authentication_classes = [JWTAuthentication]

#class anonth(AnonRateThrottle):
#    rate = '60/min'

class LvmsgVS(ModelViewSet):
  queryset = Lvmsg.objects.all()
  serializer_class = LvmsgSl
  throttle_classes = [AnonRateThrottle]
  permission_classes = [IsAuthenticated]
  authentication_classes = [JWTAuthentication]