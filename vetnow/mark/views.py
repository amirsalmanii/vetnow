from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Mark
from . import serializers
from product.views import MyPagination
from product.models import Product

class ListMarkedProducts(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.MarkProductsSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        marks = Mark.objects.filter(user=self.request.user)
        return marks


class MarkedProductDelete(APIView):
    def delete(self, request, pk):
        if request.user.is_authenticated:
            try:
                product_marked = Mark.objects.get(id=pk, user=request.user)
            except:
                return Response({"detail": "Authentication credentials were not provided."}, status=401)
            else:
                product_marked.delete()
                return Response(status=204)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=401)


class CreateOrRemoveMarkProduct(APIView):
    """
    Here, if the user selects a product for his favorites,
    if it already exists, he will delete the relationship, and if there is no 
    relationship, he will add it to his favorites list.
    """
    def get(self, request, pk):
        if request.user.is_authenticated:
            product = Product.objects.get(id=pk)
            is_exists = Mark.objects.filter(user=request.user, product=product)
            if is_exists:
                marked = is_exists.first()
                marked.delete()
                return Response('delete product from favs', status=204)
            else:
                Mark.objects.create(user=request.user, product=product)
                return Response('added to marks', status=201)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=401)         
