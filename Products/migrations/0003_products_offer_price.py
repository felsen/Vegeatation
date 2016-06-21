# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_products_usercartproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='offer_price',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
