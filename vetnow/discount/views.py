from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Discount
from . import serializers
from product.views import MyPagination
# YYYY-MM-DD


class DiscountListView(ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountListSerializer
    pagination_class = MyPagination


class DiscountCreateView(CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountCreateSerializer
    pagination_class = MyPagination


class DiscountUpdateView(RetrieveUpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountCreateSerializer


class DiscountDetailView(RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountListSerializer


class DiscountDeletView(DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountCreateSerializer