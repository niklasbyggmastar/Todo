# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=50)),
                ('todo_done', models.BooleanField(default=0)),
            ],
        ),
    ]
