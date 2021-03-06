# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.BooleanField(default=False),
        ),
    ]
