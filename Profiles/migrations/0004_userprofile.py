# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_no', models.CharField(max_length=12)),
                ('gender', models.IntegerField(default=None, choices=[(1, b'Male'), (2, b'Female')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
