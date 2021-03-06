# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160115151452 on 2016-07-09 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0027_auto_20160709_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmark',
            name='count_in_scoreboard',
            field=models.ManyToManyField(blank=True, related_name='count_in_scoreboard', to='competitions.Competition'),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='is_scalar',
            field=models.BooleanField(default=True),
        ),
    ]
