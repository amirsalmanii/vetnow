# Generated by Django 3.2 on 2021-12-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20211222_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]