# Generated by Django 3.2 on 2021-12-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20211228_0727'),
        ('order', '0007_alter_order_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='orders_c', to='product.Category'),
        ),
    ]