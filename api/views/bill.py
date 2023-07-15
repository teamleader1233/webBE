from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from ..models.bill import Bill
from ..serializers.bill import BillSerializer


class BillViewSet(ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()
    permission_classes = [IsAdminUser]