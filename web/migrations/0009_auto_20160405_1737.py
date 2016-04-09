# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0008_auto_20160318_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tramite',
            name='user',
        ),
        migrations.AddField(
            model_name='tramite',
            name='users',
            field=models.ManyToManyField(related_name='tramites', to=settings.AUTH_USER_MODEL),
        ),
    ]