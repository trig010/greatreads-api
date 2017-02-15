# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greatreads', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Search',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='search',
        ),
        migrations.RenameField(
            model_name='input',
            old_name='question',
            new_name='search',
        ),
        migrations.RenameField(
            model_name='search',
            old_name='question_text',
            new_name='search_text',
        ),
    ]
