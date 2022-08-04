# Generated by Django 4.0.6 on 2022-08-04 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survivor', '0003_item_alter_survivor_infected'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantidade:')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survivor.item')),
                ('survivor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survivor.survivor')),
            ],
            options={
                'verbose_name': 'Inventário',
                'verbose_name_plural': 'Inventários',
                'ordering': ['id'],
            },
        ),
    ]