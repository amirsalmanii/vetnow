# Generated by Django 3.2 on 2021-12-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20211214_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ilked',
            new_name='like',
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]