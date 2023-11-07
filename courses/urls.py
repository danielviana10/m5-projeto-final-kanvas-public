from contents.views import CreateContentView, RetrieveUpdateDestroyContentView
from courses.views import (
    AddStudentToCourse,
    CreateListCourseView,
    DeleteStudentFromCourseView,
    RetrieveUpdateDestroyCourseView,
)
from django.urls import path


urlpatterns = [
    path("courses/", CreateListCourseView.as_view()),
    path(
        "courses/<uuid:course_id>/", RetrieveUpdateDestroyCourseView.as_view()
    ),  # noqa
    path("courses/<uuid:course_id>/contents/", CreateContentView.as_view()),
    path(
        "courses/<uuid:course_id>/contents/<uuid:content_id>/",
        RetrieveUpdateDestroyContentView.as_view(),
    ),
    path("courses/<uuid:course_id>/students/", AddStudentToCourse.as_view()),
    path(
        "courses/<uuid:course_id>/students/<uuid:student_id>/",
        DeleteStudentFromCourseView.as_view(),
    ),
]
