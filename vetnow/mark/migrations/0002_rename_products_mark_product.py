# Generated by Django 3.2 on 2022-01-29 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='products',
            new_name='product',
        ),
    ]