# Generated by Django 4.2.4 on 2023-11-07 01:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("courses", "0001_initial"),
        ("students_courses", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                related_name="my_courses",
                through="students_courses.StudentCourse",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
