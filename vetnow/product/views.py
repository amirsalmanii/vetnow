import codecs
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .models import Category, Product
from . import serializers
from rest_framework.permissions import IsAdminUser


class MyPagination(PageNumberPagination):
    page_size = 20


class CategoriesWithPaginationView(ListAPIView):
    queryset = Category.objects.filter()# parent__isnull=True
    serializer_class = serializers.CategoriesSerializer
    pagination_class = MyPagination
    # permission_classes = (permissions.AdminOrEmployee,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoriesListView(ListAPIView):
    queryset = Category.objects.filter()
    serializer_class = serializers.CategoriesSerializer

class CategoriesForMainPageListView(ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = serializers.CategoriesSerializer


class CreateCategory(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryAddAndUpdateSerializer
    permission_classes = (IsAdminUser,)


class UpdateCategory(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryAddAndUpdateSerializer
    lookup_field = "slug"
    permission_classes = (IsAdminUser,)


class DeleteCategory(DestroyAPIView):
    """
    this class get category slug and delete category
    """
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryAddAndUpdateSerializer
    lookup_field = 'slug'
    permission_classes = (IsAdminUser,)


class ProductsListPaginationView(ListAPIView):
    """
    see get_queryset func document
    """
    serializer_class = serializers.ProductsSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'descreption']

    def get_queryset(self):
        products = Product.objects.filter(hide=False)
        return products


class ProductDetaiView(APIView):
    def get(self, request, slug):
        product = Product.objects.is_exist_product(slug)
        if not product:
            return Response(status=404)
        serializer = serializers.ProductsSerializer(product, context={'request': request})
        return Response(serializer.data)


class ProductPdfDownload(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except:
            pass
        else:
            pdf = product.pdf_file.path
            with codecs.open(pdf, 'r', encoding='utf-8', errors='ignore') as file:
                response = HttpResponse(file, content_type='text/pdf')
                response['Content-Disposition'] = 'attachment; filename=file.pdf'
                return response


class ProductsListView(ListAPIView):
    queryset = Product.objects.filter()
    serializer_class = serializers.ProductsSerializer


class ProductByCategory(ListAPIView):
    serializer_class = serializers.ProductsSerializer

    def get_queryset(self):
        products = Product.objects.filter(hide=False)
        return products


class ProductDelete(APIView):
    permission_classes = (IsAdminUser,)

    def delete(self, request, slug):
        product = Product.objects.is_exist_product(slug)
        if product:
            product.hide = True
            product.save()
            return Response(status=204)
        else:
            return Response(status=404)


class ProductUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
    serializer_class = serializers.ProductUpdateSerializer
    permission_classes = (IsAdminUser,)


class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductUpdateSerializer
    permission_classes = (IsAdminUser,)


class SayProductQuntity(APIView):
    def get(self, request, pk, client_quantity):
        try:
            product = Product.objects.get(id=pk)
        except:
            return Response(status=404)
        else:
            quantity_product = product.quantity #10
            result = quantity_product - client_quantity
            if result >= 0:
                return Response(status=200)
            return Response({f'{product.name}: تعداد خواسته شده شما بیشتر از موجودی انبار است تعداد را چک کنید'}, status=400)