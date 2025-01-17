from rest_framework import serializers

from students_courses.models import StudentCourse


class StudentCourseSerializer(serializers.ModelSerializer):
    students_courses = serializers.CharField(
        write_only=True, source="course.id"
    )  # noqa
    student_id = serializers.CharField(read_only=True, source="student.id")
    student_username = serializers.CharField(
        read_only=True, source="student.username"
    )  # noqa
    student_email = serializers.CharField(source="student.email")

    class Meta:
        model = StudentCourse
        fields = [
            "id",
            "students_courses",
            "student_id",
            "student_username",
            "student_email",
            "status",
        ]
