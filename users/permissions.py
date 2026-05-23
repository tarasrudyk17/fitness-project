from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Дозвіл лише для користувачів з роллю 'admin'
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'admin'
        )

from rest_framework import permissions

class IsAdminOrReadOnlyForClients(permissions.BasePermission):
    """
    Дозволяє повний доступ адміністраторам,
    клієнтам — лише читання (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.userprofile.role == 'admin'
