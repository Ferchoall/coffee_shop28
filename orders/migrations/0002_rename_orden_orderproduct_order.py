# Generated by Django 5.1 on 2024-08-30 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='orden',
            new_name='order',
        ),
    ]
