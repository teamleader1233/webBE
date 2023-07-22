from rest_framework.viewsets import ModelViewSet

from ..models.product import Product
from ..serializers.product import ProductSerializer
from ..utils.permission import IsAdminUserOrReadOnly


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    #permission_classes = [IsAdminUserOrReadOnly]
    search_fields = []
    ordering_fields = ['name', 'price']