# Generated by Django 2.2 on 2019-06-01 15:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friend', '0002_auto_20190601_1513'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='newFriendRequest',
            new_name='FriendRequest',
        ),
    ]
