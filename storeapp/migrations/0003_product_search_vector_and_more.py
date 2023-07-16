# Generated by Django 4.1.1 on 2023-07-16 21:28

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_product_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='storeapp_pr_search__0b93e8_gin'),
        ),
    ]
