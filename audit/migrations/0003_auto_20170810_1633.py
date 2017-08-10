# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0002_auto_20170810_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='audit_log',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auditlog',
            name='log_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
