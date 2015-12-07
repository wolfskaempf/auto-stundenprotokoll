# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150711_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonprotocol',
            name='attendingStudents',
            field=models.ManyToManyField(to='core.Student'),
        ),
    ]
