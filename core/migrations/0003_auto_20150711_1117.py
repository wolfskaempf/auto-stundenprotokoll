# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150711_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='inClass',
        ),
        migrations.AddField(
            model_name='student',
            name='inClass',
            field=models.ManyToManyField(to='core.Class'),
        ),
    ]
