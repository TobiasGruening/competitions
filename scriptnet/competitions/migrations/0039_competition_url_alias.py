# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-16 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0038_individual_activation_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='url_alias',
            field=models.SlugField(default='', max_length=30),
        ),
    ]
