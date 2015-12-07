# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150713_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='rating',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]
