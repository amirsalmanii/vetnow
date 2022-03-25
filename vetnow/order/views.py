from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import Order, RefundOrdersRequest, OrderItems


User = get_user_model()


class MyPagination(PageNumberPagination):
    page_size = 20


class OrdersView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrdersSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_id']


# added product counts TODO say to frontend dev
class OrderUpdateView(APIView):
    def get(self, request, pk, order_id):
        try:
            order = Order.objects.get(id=pk)
            oid = order_id
            order_items = OrderItems.objects.filter(order_id=oid)
        except:
            return Response(status=404)
        else:
            serializer = serializers.OrdersSerializer(order)
            serializer2 = serializers.OrdersItemDetailsSerializer(order_items, many=True)
            return Response({"data1": serializer.data, "data2": serializer2.data})

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


class OrderCreateView(APIView):
    def post(self, request):
        serializer = serializers.OrdersCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class OrderItemsCreateView(APIView):
    def post(self, request):
        serializer = serializers.OrdersItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


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

class UserOrders2View(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrdersSerializer
    pagination_class = MyPagination
    def get_queryset(self):
        user = self.request.user
        orders = user.orders.all()
        return orders


class OrderUserUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, order_id):
        try:
            oid = order_id
            order = Order.objects.get(order_id=oid)
            order_items = OrderItems.objects.filter(order_id=oid)
        except:
            return Response(status=404)
        else:
            serializer = serializers.OrdersSerializer(order)
            serializer2 = serializers.OrdersItemDetailsSerializer(order_items, many=True, context={'request': request})
            return Response({"data1": serializer.data, "data2": serializer2.data})