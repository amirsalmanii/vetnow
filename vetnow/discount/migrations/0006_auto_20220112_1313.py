# Generated by Django 3.2 on 2022-01-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0005_auto_20220112_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='valid_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='valid_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
