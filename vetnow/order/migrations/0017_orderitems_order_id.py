# Generated by Django 3.2 on 2022-02-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20220201_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='order_id',
            field=models.UUIDField(default=1),
            preserve_default=False,
        ),
    ]
