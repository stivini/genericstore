# Generated by Django 4.1.7 on 2023-11-06 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_users_products_users_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='amount',
            new_name='order_amount',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='quantity',
            new_name='quantity_in_stock',
        ),
    ]
