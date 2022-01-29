from rest_framework import serializers
from .models import Mark
from product.serializers import ProductUpdateSerializer


class MarkProductsSerializer(serializers.ModelSerializer):
    product = ProductUpdateSerializer()

    class Meta:
        model = Mark
        fields = '__all__'
