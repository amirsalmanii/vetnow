# Generated by Django 3.2 on 2021-12-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_product_descreption'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer_price',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]