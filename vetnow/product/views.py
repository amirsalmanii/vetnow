from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Category, Product
from . import serializers
from ip2geotools.databases.noncommercial import DbIpCity
from accounts.models import IpTables
from rest_framework.pagination import PageNumberPagination
 

class MyPagination(PageNumberPagination):
    page_size = 2


class CategoriesView(APIView):
    """
    Because we want to get the user's IP and this view is called,
    we always use it here on the first page
    """
    def get(self, request):
        query = Category.objects.filter(parent__isnull=True)
        serializer = serializers.CategoriesSerializer(query, many=True)
        # get user ip
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # get user city
        exist = IpTables.objects.filter(ip=ip)
        if not exist:
            try:
                response = DbIpCity.get(ip, api_key='free')
                IpTables.objects.create(ip=ip, city=response.city)
            except:
                pass
        else:
            pass
        # return categories
        return Response(serializer.data, status=200)


class CreateCategory(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryAddAndUpdateSerializer


class UpdateCategory(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryAddAndUpdateSerializer
    lookup_field = "slug"


class ProductsListView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = serializers.ProductsSerializer
    pagination_class = MyPagination    


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
            products = category.products.filter(available=True)
            serializer = serializers.ProductsSerializer(products, many=True)
        except:
            return Response(status=404)
        return Response(serializer.data, status=200)


class ProductDelete(APIView):
    def delete(self, request, slug):
        product = Product.objects.is_exist_product(slug)
        if product:
            product.available = False
            product.save()
            return Response(status=204)
        else:
            return Response(status=404)


class ProductUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
    serializer_class = serializers.ProductUpdateSerializer


class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductUpdateSerializer
