# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-21 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beeflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='role',
            field=models.ManyToManyField(to='beeflow.FlowRole', verbose_name='审批角色'),
        ),
    ]
