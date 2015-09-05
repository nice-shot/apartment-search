# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.CharField(serialize=False, max_length=100, primary_key=True)),
                ('message', models.TextField()),
                ('user', models.CharField(max_length=300)),
                ('likes', models.PositiveIntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('found', models.DateTimeField()),
                ('interesting', models.NullBooleanField()),
            ],
        ),
    ]
