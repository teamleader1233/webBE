from rest_framework import serializers

from secrets import token_urlsafe

from ..models.bill import Bill


class BillSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Bill
        fields = '__all__'
        extra_kwargs = {
            'total': {'read_only': True},
        }