# Generated by Django 4.0.6 on 2022-08-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survivor', '0005_remove_inventory_item_inventory_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivor',
            name='latitude',
            field=models.FloatField(max_length=100, verbose_name='Latitude:'),
        ),
        migrations.AlterField(
            model_name='survivor',
            name='longitude',
            field=models.FloatField(max_length=100, verbose_name='Longitude:'),
        ),
    ]
