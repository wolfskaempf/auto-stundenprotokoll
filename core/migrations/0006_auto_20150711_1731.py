# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150711_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='lastPaid',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(),
        ),
    ]
