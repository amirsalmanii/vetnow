# Generated by Django 3.2 on 2021-12-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255, null=True, unique=True),
        ),
    ]
