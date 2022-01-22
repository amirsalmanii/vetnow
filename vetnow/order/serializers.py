from rest_framework import serializers
from order.models import Order
from product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class UserSerilizer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    product = ProductSerilizer(many=True)
    owner = UserSerilizer()
    class Meta:
        model = Order
        fields = '__all__'


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('owner', 'product')
