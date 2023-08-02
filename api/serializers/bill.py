from rest_framework import serializers

from ..models.bill import Bill


class BillSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Bill
        fields = '__all__'
        read_only_fields = ['total']