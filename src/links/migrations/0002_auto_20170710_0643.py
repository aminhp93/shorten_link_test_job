# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shortlink',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
