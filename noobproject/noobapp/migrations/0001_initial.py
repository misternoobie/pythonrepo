# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='friend',
            fields=[
                ('slug', models.SlugField(unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=120)),
                ('Address', models.TextField(blank=True)),
                ('Birthday', models.DateField(blank=True)),
                ('Image', models.ImageField(blank=True, upload_to=b'')),
                ('Email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'verbose_name': 'Name List',
            },
        ),
    ]