from rest_framework import serializers

from ..models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=80)
    price = serializers.IntegerField(min_value=1, max_value=1000000000, default=1)
    description = serializers.CharField(max_length=200)
    image = serializers.ImageField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image')