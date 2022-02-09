from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Mark
from . import serializers
from product.views import MyPagination


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

# im use product detail view for detail marked products