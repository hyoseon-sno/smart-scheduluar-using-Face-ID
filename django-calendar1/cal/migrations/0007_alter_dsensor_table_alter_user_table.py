# Generated by Django 4.2.1 on 2023-06-06 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0006_alter_dsensor_table_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dsensor',
            table='dsensor',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user_data',
        ),
    ]
