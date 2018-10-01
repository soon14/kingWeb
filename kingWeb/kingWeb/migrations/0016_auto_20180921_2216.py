# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-21 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kingWeb', '0015_auto_20180921_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systablecolumn',
            old_name='table',
            new_name='tableid',
        ),
        migrations.AlterField(
            model_name='systablecolumn',
            name='tableid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kingWeb.SysTableList'),
        ),
    ]