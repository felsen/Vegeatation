# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('images', models.ImageField(upload_to=b'static/images')),
                ('active', models.BooleanField(default=False)),
                ('order', models.IntegerField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
