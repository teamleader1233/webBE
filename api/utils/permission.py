from rest_framework.permissions import BasePermission


class IsAdminUserOrReadOnly(BasePermission):
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_permission(self, request, view):
        if (request.method in self. SAFE_METHODS 
            or request.user.is_staff):
            return True
        return False