# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]