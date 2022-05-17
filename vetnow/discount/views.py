from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Discount
from . import serializers
from product.views import MyPagination
# YYYY-MM-DD


class DiscountListView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountListSerializer
    pagination_class = MyPagination


class DiscountCreateView(APIView):
    def post(self, request):
        serializer = serializers.DiscountCreateSerializer(data=request.data)
        if serializer.is_valid():
            print('yes')
            data = serializer.validated_data
            products = data['products']
            percent = data['discount_percent']
            for pr in products:
                pr.price_after_discount = pr.price - (1 / 100) * percent * pr.price
                pr.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class DiscountUpdateView(APIView):
    def put(self, request, pk):
        discount = Discount.objects.get(id=pk)
        serializer = serializers.DiscountCreateSerializer(instance=discount, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            products = data['products']
            percent = data['discount_percent']
            for pr in products:
                pr.price_after_discount = pr.price - (1 / 100) * percent * pr.price
                pr.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class DiscountDetailView(RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountListSerializer


class DiscountDeletView(DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountCreateSerializer