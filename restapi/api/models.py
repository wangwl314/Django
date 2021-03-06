# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Category(models.Model):
  cateName = models.CharField(max_length=30, primary_key=True)


class Article(models.Model):
  title = models.CharField(max_length=50)
  text = models.TextField(default='')
  cate = models.ForeignKey('Category', on_delete=models.RESTRICT)
  active = models.CharField(choices=[('yes','Y'),('no','N')], default='no', max_length=5)
  insTime = models.DateTimeField(auto_now=True)

class Lvmsg(models.Model):
  content = models.CharField(max_length=200, default='')
  nikename = models.CharField(max_length=20)
  created = models.DateTimeField(auto_now=True)