# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-20 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180221_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile-pictures/'),
        ),
    ]
