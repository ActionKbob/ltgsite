# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='keywords',
            field=models.CharField(default='test, key, words', max_length=100),
            preserve_default=False,
        ),
    ]
