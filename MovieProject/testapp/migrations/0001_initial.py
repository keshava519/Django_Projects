# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-01-05 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateField()),
                ('moviename', models.CharField(max_length=30)),
                ('hero', models.CharField(max_length=30)),
                ('heroine', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]