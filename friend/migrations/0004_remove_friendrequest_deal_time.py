# Generated by Django 2.2 on 2019-06-02 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0003_auto_20190601_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='deal_time',
        ),
    ]