# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]