# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_lessonprotocol_attendingstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('protocol', models.TextField()),
                ('attendingStudents', models.ManyToManyField(to='core.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='lessonprotocol',
            name='attendingStudents',
        ),
        migrations.RemoveField(
            model_name='lessonprotocol',
            name='inClass',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='lastPaidFor',
            new_name='lastPaid',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='className',
            new_name='name',
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.CharField(default='Tom Wolfsk\xe4mpf', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LessonProtocol',
        ),
        migrations.AddField(
            model_name='lesson',
            name='inClass',
            field=models.ForeignKey(to='core.Class'),
        ),
    ]
