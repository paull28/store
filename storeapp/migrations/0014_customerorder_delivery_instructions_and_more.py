# Generated by Django 4.1.1 on 2023-07-20 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0013_remove_customerorder_delivery_customerorder_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='delivery_instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 19, 42, 31, 94059)),
        ),
    ]