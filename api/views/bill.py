from rest_framework.viewsets import ModelViewSet, ViewSet

from ..models.bill import Bill
from ..serializers.bill import BillSerializer
from ..utils.permission import IsAdminUserOrRetrieveOnly


class BillViewSet(ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()
    permission_classes = [IsAdminUserOrRetrieveOnly]
    search_fields = ['product__id', 'status']
    ordering_fields = ['quantity', 'date', 'total']