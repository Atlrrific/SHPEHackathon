# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 00:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pub_date',
        ),
    ]
