# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0028_auto_20160709_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='uploads/avatars/'),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='subtracks',
            field=models.ManyToManyField(blank=True, to='competitions.Subtrack'),
        ),
    ]
