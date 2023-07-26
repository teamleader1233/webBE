from rest_framework.serializers import ModelSerializer

from ..models.blog import Blog


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')