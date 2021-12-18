from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Category, Product
from . import serializers


class CategoriesView(APIView):
    def get(self, request):
        query = Category.objects.filter(parent__isnull=True)
        serializer = serializers.CategoriesSerializer(query, many=True)
        return Response(serializer.data, status=200)


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializer


class ProductDetaiView(APIView):
    def get(self, request, slug):
        product = Product.objects.is_exist_product(slug)
        if not product:
            return Response(status=404)
        serializer = serializers.ProductsSerializer(product, context={'request': request})
        return Response(serializer.data)


class ProductByCategory(APIView):
    def get(self, request, slug):
        try:
            category = Category.objects.filter(slug=slug).first()
            products = category.products.all()
            serializer = serializers.ProductsSerializer(products, many=True)
        except:
            return Response(status=404)
        return Response(serializer.data, status=200)
