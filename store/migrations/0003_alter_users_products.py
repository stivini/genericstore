# Generated by Django 4.1.7 on 2023-10-01 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_users_options_alter_users_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='products',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='store.products'),
        ),
    ]