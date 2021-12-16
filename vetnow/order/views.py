from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Order
from django.contrib.auth import get_user_model

User = get_user_model()


class OrdersView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
        except:
            return Response(status=404)
        serializer = serializers.OrdersSerializer(orders, many=True)
        return Response(serializer.data)


class UserOrdersView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            orders = user.orders.all()
        except:
            return Response(status=404)
        serializer = serializers.OrdersSerializer(orders, many=True)
        return Response(serializer.data)


