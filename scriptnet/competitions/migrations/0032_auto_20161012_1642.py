# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0031_auto_20161012_1623'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PublicLinks',
            new_name='PublicLink',
        ),
    ]