# Generated by Django 4.2.17 on 2025-01-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_activity_end_date_alter_activity_start_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="visitmedia",
            name="main_pic",
            field=models.BooleanField(default=False),
        ),
    ]
