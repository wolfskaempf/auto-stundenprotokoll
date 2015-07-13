# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150711_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='attendingStudents',
            field=models.ManyToManyField(to='core.Student', blank=True),
        ),
    ]
