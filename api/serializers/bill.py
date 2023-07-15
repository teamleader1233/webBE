from rest_framework import serializers

from ..models.bill import Bill, Product


class BillSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=False)
    quantity = serializers.IntegerField(min_value=1, max_value=100, default=1)
    status = serializers.ChoiceField(choices=Bill.STATUS_CHOICES, default='pending')
    address = serializers.CharField(max_length=80)
    payment = serializers.ChoiceField(choices=Bill.PAYMENT_CHOICES, default='cod')
    
    class Meta:
        model = Bill
        fields = ('id', 'product', 'quantity', 'status', 'address', 'payment')
        extra_kwargs = {
            'updated_at': {'read_only': True},
        }