# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMSApp', '0011_noticeboard_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomallotment',
            name='room_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]