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
    page_size = 2


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
        """
        this functin return list of products
        but
        in this way we check discount time is valid if valid we send with product list
        if it doesn't valid we send 0 in discount_after_price field (means we dont have any discunt)
        """
        now = timezone.now().date()
        products = Product.objects.filter()
        for pr in products:
            if pr.price_after_discount > 0:
                if pr.pdiscount.all():
                    # means we have discount object in discount model
                    for discount in pr.pdiscount.all():
                        # check discount date is valid
                        if discount.valid_to < now:
                            pr.price_after_discount = 0
                            pr.save()
                else:
                    # means if this product dont have any discount object
                    # we can set value to 0
                    pr.price_after_discount = 0
                    pr.save()
        return products


class ProductDetaiView(APIView):
    def get(self, request, slug):
        product = Product.objects.is_exist_product(slug)
        if not product:
            return Response(status=404)
        serializer = serializers.ProductsSerializer(product, context={'request': request})
        return Response(serializer.data)


class ProductsListView(ListAPIView):
    queryset = Product.objects.filter()
    serializer_class = serializers.ProductsSerializer


class ProductByCategory(ListAPIView):
    serializer_class = serializers.ProductsSerializer

    def get_queryset(self):
        ##############################################################
        # check discount validation
        now = timezone.now().date()
        products = Product.objects.filter()
        for pr in products:
            if pr.price_after_discount > 0:
                if pr.pdiscount.all():
                    # means we have discount object in discount model
                    for discount in pr.pdiscount.all():
                        # check discount date is valid
                        if discount.valid_to < now:
                            pr.price_after_discount = 0
                            pr.save()
                else:
                    # means if this product dont have any discount object
                    # we can set value to 0
                    pr.price_after_discount = 0
                    pr.save()
        ##############################################################
        slug = self.kwargs['slug']
        try:
            category = Category.objects.filter(slug=slug).first()
            products = category.products.all()
        except:
            return None
        return products


class ProductDelete(APIView):
    permission_classes = (IsAdminUser,)

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
    permission_classes = (IsAdminUser,)


class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductUpdateSerializer
    permission_classes = (IsAdminUser,)
