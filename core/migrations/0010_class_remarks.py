# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_class_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]
