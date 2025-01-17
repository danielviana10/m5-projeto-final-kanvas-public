from django.db import models
import uuid


class StatusChoices(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.NOT_STARTED,
        max_length=11,  # noqa
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,  # noqa
    )
    students = models.ManyToManyField(
        "accounts.account",
        through="students_courses.StudentCourse",
        related_name="my_courses",
    )
