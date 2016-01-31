# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0, max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='view',
            field=models.IntegerField(default=0, max_length=128),
            preserve_default=True,
        ),
    ]
