from rest_framework.permissions import BasePermission


class IsAdminUserOrRetrieveOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action != 'retrieve' and not request.user.is_staff:
            return False
        return True