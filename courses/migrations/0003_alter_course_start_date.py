# Generated by Django 4.2.4 on 2023-11-07 01:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="start_date",
            field=models.DateField(),
        ),
    ]
