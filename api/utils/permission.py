from rest_framework.permissions import BasePermission


class IsAdminUserOrRetrieveOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action != 'retrieve' and (not request.user or not request.user.is_staff):
            return False
        return True
    
class IsAdminUserOrReadOnly(BasePermission):
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_permission(self, request, view):
        if request.method in self.SAFE_METHODS or (request.user and request.user.is_staff):
            return True
        return False