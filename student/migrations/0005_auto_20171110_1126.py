# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 08:26
from __future__ import unicode_literals

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20171103_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=fernet_fields.fields.EncryptedCharField(max_length=200),
        ),
    ]
