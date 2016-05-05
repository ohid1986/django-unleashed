# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(related_name='blog_posts', to='organizer.Startup', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='blog_posts', to='organizer.Tag', blank=True),
        ),
    ]
