# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0005_newslink_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together=set([('slug', 'startup')]),
        ),
    ]
