# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATE', models.DateField()),
                ('TIME', models.TextField()),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
