# Generated by Django 4.1.1 on 2023-07-16 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_product_search_vector_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='product',
            name='storeapp_pr_search__0b93e8_gin',
        ),
        migrations.RemoveField(
            model_name='product',
            name='search_vector',
        ),
    ]
