# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('full_description', models.CharField(max_length=255)),
                ('units', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Datapoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('reps', models.PositiveIntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('activity', models.ForeignKey(to='stats.Activity')),
            ],
        ),
    ]
