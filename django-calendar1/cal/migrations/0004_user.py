# Generated by Django 4.2 on 2023-06-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cal", "0003_alter_dsensor_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "time",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("user", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "user_data",
            },
        ),
    ]
