from rest_framework.viewsets import ModelViewSet

from ..models.blog import Blog
from ..serializers.blog import BlogSerializer
from ..utils.permission import IsAdminUserOrReadOnly


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    ordering_fields = ['-created_at', '-updated_at']