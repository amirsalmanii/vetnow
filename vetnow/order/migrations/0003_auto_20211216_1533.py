# Generated by Django 3.2 on 2021-12-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_material'),
        ('order', '0002_auto_20211216_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='order_detail', to='product.Product'),
        ),
    ]