# Generated by Django 5.1.2 on 2024-10-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_address_remove_order_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]