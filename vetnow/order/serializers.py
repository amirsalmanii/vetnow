from rest_framework import serializers
from order.models import Order, RefundOrdersRequest, OrderItems
from product.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()

class ProductSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'image', 'descreption', 'manufacturer_company')


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


class OrdersCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ('owner',)


class OrdersItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = '__all__'


class OrdersItemDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerilizer()

    class Meta:
        model = OrderItems
        fields = '__all__'


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('owner', 'product')


class OrderRefundsSerializer(serializers.ModelSerializer):
    user = UserSerilizer(read_only=True)
    class Meta:
        model = RefundOrdersRequest
        fields = '__all__'


class OrderRefundUpdateSerializer(serializers.ModelSerializer):
    user = UserSerilizer(read_only=True)
    class Meta:
        model = RefundOrdersRequest
        fields = ['user', 'Confirmation']