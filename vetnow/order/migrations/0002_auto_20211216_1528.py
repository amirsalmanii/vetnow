# Generated by Django 3.2 on 2021-12-16 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_material'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='product.product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]
