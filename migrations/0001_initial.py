# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
                ('gdate', models.DateField()),
                ('ggirlnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
                ('isdelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sage', models.IntegerField()),
                ('sinfo', models.CharField(max_length=100)),
                ('isdelete', models.BooleanField()),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LX.Grade')),
            ],
        ),
    ]
