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
        fields = ('username', 'first_name', 'last_name', 'state')


class OrdersSerializer(serializers.ModelSerializer):
    product = ProductSerilizer(many=True)
    owner = UserSerilizer()
    class Meta:
        model = Order
        fields = '__all__'
