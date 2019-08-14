# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-02-09 08:18
from __future__ import unicode_literals

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255, verbose_name='태그'),
        ),
    ]
