# Generated by Django 3.2 on 2022-02-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_orderitems_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='c_price',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
