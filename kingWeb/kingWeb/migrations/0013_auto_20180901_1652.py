# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-01 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kingWeb', '0012_auto_20180901_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sysrolemenu',
            old_name='menuid',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='sysrolemenu',
            old_name='roleid',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='sysuserdepartment',
            old_name='departmentid',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='sysuserdepartment',
            old_name='userid',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='sysuserrole',
            old_name='roleid',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='sysuserrole',
            old_name='userid',
            new_name='user',
        ),
    ]
