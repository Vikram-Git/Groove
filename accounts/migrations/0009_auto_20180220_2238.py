# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-20 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180220_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='profile-pictures'),
        ),
    ]
