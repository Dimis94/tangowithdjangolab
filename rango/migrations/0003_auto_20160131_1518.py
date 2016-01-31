# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20160131_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='view',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
