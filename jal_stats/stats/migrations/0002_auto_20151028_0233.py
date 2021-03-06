# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'ordering': ['-date']},
        ),
        migrations.AlterUniqueTogether(
            name='stat',
            unique_together=set([('activity', 'date')]),
        ),
    ]
