# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-14 22:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myrestaurants', '0003_auto_20170412_2202'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='restaurantreview',
            unique_together=set([('restaurant', 'user')]),
        ),
    ]
