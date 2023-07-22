from rest_framework import serializers

from ..models.bill import Bill


class BillSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Bill
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'total': {'read_only': True},
            'updated_at': {'read_only': True},
        }