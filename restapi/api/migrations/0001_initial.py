# Generated by Django 3.1.2 on 2020-10-18 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cateName', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lvmsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(default='')),
                ('actvie', models.BooleanField(default=False)),
                ('insTime', models.DateTimeField(auto_now=True)),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.category')),
            ],
        ),
    ]
