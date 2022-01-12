from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Discount
from . import serializers


class DiscuntCreate(ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscuntCreateSerializer
