from rest_framework import serializers
from .models import Mark
from product.serializers import ProductsSerializer


class MarkProductsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = Mark
        fields = '__all__'
