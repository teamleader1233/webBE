from rest_framework.serializers import ModelSerializer

from ..models.blog import Blog


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': True},
            'content': {'required': True},
        }