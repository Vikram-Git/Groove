# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-20 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180220_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='/static/accounts/img/user.jpg', upload_to='profile-pictures'),
        ),
    ]
