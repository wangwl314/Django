# Generated by Django 3.1.2 on 2020-10-22 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_lvmsg_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lvmsg',
            old_name='user',
            new_name='nikename',
        ),
    ]
