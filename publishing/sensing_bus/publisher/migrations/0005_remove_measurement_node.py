# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0004_auto_20170407_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='node',
        ),
    ]