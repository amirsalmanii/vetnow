# Generated by Django 3.2 on 2022-01-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_product_price_after_discount'),
        ('discount', '0004_auto_20220112_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='products',
        ),
        migrations.AddField(
            model_name='discount',
            name='products',
            field=models.ManyToManyField(related_name='pdiscount', to='product.Product'),
        ),
    ]
