from typing import Any
from rest_framework.viewsets import ModelViewSet

from ..models.bill import Bill
from ..serializers.bill import BillSerializer
from ..utils.permission import IsAdminUserOrRetrieveOnly


class BillViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrRetrieveOnly]
    serializer_class = BillSerializer
    queryset = Bill.objects.all()