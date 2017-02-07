# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Zmfen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZmScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=30)),
                ('certno', models.CharField(max_length=20)),
                ('score', models.IntegerField()),
                ('uuidfield', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
    ]
