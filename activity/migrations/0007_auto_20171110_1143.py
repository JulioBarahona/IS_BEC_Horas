# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 08:43
from __future__ import unicode_literals

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_auto_20171110_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='time_worth',
            field=fernet_fields.fields.EncryptedIntegerField(default=1),
        ),
    ]
