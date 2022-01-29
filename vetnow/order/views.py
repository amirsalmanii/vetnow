from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from . import serializers
from .models import Order, RefundOrdersRequest


User = get_user_model()


class MyPagination(PageNumberPagination):
    page_size = 2


class OrdersView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrdersSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_id']


class OrderUpdateView(APIView):
    def get(self, request, pk):
        try:
            order = Order.objects.get(id=pk)
        except:
            return Response(status=404)
        else:
            serializer = serializers.OrdersSerializer(order)
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            order = Order.objects.get(id=pk)
        except:
            return Response(status=404)
        else:
            serializer = serializers.OrderUpdateSerializer(instance=order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors)


class OrdersStatusCountView(APIView):
    """
    return all orders count if status is refund or ...
    """
    def get(self, request):
        orders_refund_counts = Order.objects.filter(payment_status='r').count()
        orders_pending_ounts = Order.objects.filter(payment_status='p', confirmation=False).count()
        return Response({"refunds_count": orders_refund_counts, 'pending_orders': orders_pending_ounts}, status=200)


class RefundsOrdersRequestView(ListAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundsSerializer
    pagination_class = MyPagination


class RefundOrderRequestDetailView(RetrieveAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundsSerializer


class RefundOrderRequestUpdateView(UpdateAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundUpdateSerializer


# ################users orders request


class UserOrdersView(APIView):
    def get(self, request):
        try:
            user = request.user
            orders = user.orders.all()
        except:
            return Response(status=404)
        serializer = serializers.OrdersSerializer(orders, many=True)
        return Response(serializer.data)