# Generated by Django 3.2.24 on 2025-02-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20250212_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='owners_flat', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
