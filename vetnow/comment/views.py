from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from product.models import Product


class CommentsView(APIView):
    def get(self, request, slug):
        try:
            product = Product.objects.is_exist_product(slug)
        except:
            return Response(status=404)
        product_comments = product.comments.filter(approved=True)
        serializer = serializers.CommentsSerializer(product_comments, many=True)
        return Response(serializer.data)

