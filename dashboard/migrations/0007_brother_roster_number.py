# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-19 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_chapterevent_eventexcuse_serviceevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='brother',
            name='roster_number',
            field=models.IntegerField(default=1856, max_length=5),
        ),
    ]