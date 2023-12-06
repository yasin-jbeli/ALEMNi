from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Implement logic to check if the user is an admin or read-only
        # Example logic:
        return request.user and request.user.role == 'admin'