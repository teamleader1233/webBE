from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


class UserViewSet(ViewSet):
    permission_classes = [IsAdminUser]
    hhtp_method_names = ['post']
    
    def create(self, request):
        return Response()