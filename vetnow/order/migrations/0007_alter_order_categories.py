# Generated by Django 3.2 on 2021-12-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20211228_0727'),
        ('order', '0006_alter_order_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='categories',
            field=models.ManyToManyField(null=True, related_name='orders_c', to='product.Category'),
        ),
    ]