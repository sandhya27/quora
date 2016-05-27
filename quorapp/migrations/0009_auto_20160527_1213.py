# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 12:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quorapp', '0008_auto_20160527_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 5, 27, 12, 13, 5, 476569, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 5, 27, 12, 13, 5, 476776, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]