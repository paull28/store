# Generated by Django 4.1.1 on 2023-07-19 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0011_alter_customerorder_date_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 19, 20, 36, 54, 512401)),
        ),
    ]
