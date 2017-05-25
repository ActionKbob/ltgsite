# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_member_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='normalPortrait',
            field=models.ImageField(blank=True, null=True, upload_to='images/memberPortraits/'),
        ),
        migrations.AddField(
            model_name='member',
            name='pixelPortrait',
            field=models.ImageField(blank=True, null=True, upload_to='images/memberPortraits/'),
        ),
    ]
