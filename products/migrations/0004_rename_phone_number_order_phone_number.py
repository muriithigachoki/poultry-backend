# Generated by Django 5.0.3 on 2024-03-26 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_phone_number_order_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone_number',
            new_name='Phone_number',
        ),
    ]
