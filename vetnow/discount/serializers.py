from rest_framework import serializers
from .models import Discount
from product.serializers import ProductUpdateSerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['categories']


class DiscountListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Discount
        fields = '__all__'


class DiscountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

