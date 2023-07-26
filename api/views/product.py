from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from ..models.product import Product
from ..serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]
    search_fields = []
    ordering_fields = ['name', 'price']