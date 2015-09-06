# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_auto_20150905_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
