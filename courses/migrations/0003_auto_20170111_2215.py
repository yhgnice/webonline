# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-11 14:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170111_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 11, 22, 15, 50, 907000), verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 11, 22, 15, 50, 907000), verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
    ]
