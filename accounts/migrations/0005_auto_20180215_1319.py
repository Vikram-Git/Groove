# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-15 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180210_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
