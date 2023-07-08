from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from django.contrib.auth import models
from django.contrib.auth.password_validation import validate_password

from uuid import uuid4

from ..models.user import Customer


class RegisterCustomerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def create(self, validated_data):
        user = Customer.objects.create(
            uuid = uuid4(),
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.username = user.get_full_name()
        user.set_password(validated_data['password'])
        user.save()
        return user