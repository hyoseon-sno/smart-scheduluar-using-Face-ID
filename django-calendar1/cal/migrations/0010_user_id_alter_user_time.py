# Generated by Django 4.2.1 on 2023-06-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0009_remove_user_id_alter_user_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
