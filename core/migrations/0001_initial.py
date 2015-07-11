# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.CharField(max_length=100)),
                ('identifier', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('lastPaidFor', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LessonProtocol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protocolDate', models.DateTimeField(auto_now_add=True)),
                ('protocolText', models.TextField()),
                ('inClass', models.ForeignKey(to='core.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('inClass', models.ForeignKey(to='core.Class')),
            ],
        ),
    ]
