from rest_framework import serializers
from .models import Discount


class DiscountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'
