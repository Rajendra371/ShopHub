# Generated by Django 5.0.1 on 2024-09-29 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]