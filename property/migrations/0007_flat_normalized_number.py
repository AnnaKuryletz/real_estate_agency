# Generated by Django 5.1.6 on 2025-02-18 12:00

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='normalized_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
    ]
