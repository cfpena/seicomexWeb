# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-17 00:36
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170516_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='noticia',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]