# Generated by Django 4.1.1 on 2023-07-20 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0014_customerorder_delivery_instructions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 20, 19, 12, 529218)),
        ),
    ]