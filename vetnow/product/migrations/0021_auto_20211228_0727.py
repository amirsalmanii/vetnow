# Generated by Django 3.2 on 2021-12-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20211225_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer_price',
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer_company',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
