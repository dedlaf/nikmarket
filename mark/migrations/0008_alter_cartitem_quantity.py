# Generated by Django 4.2.13 on 2024-06-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0007_remove_cart_prod_remove_cart_total_amount_cartitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
