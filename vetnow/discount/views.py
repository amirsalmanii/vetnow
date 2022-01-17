from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Discount
from . import serializers

# YYYY-MM-DD


class DiscountCreateView(ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountCreateSerializer


class DiscountUpdateView(RetrieveUpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountCreateSerializer
