# Generated by Django 4.1.1 on 2023-07-18 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0007_deliveryaddress_alter_customerorder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 18, 20, 32, 58, 151518)),
        ),
    ]
