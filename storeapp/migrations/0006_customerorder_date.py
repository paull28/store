# Generated by Django 4.1.1 on 2023-07-17 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0005_customerorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 17, 19, 17, 12, 628630)),
        ),
    ]