# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_comment', models.CharField(max_length=200)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Todo')),
            ],
        ),
    ]