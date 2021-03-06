# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_class_remarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='lastPaid',
            new_name='last_paid',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='attendingStudents',
            new_name='attending_students',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='inClass',
            new_name='in_class',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='inClass',
            new_name='in_class',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
