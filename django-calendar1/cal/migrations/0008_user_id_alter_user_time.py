# Generated by Django 4.2.1 on 2023-06-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0007_alter_dsensor_table_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
