# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMSApp', '0006_complaint_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomallotment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
