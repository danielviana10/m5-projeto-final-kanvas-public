from rest_framework import permissions

from contents.models import Content

from rest_framework.views import View


class AccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Content) -> bool:
        if (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
        ):
            return True
        return request.user.is_authenticated and request.user.is_superuser
