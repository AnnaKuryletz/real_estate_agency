# Generated by Django 5.1.6 on 2025-02-18 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20250218_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='normalized_number',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
