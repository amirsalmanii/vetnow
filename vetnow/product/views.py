from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from . import serializers


class CategoriesView(APIView):
    def get(self, request):
        query = Category.objects.filter(parent__isnull=True)
        serializer = serializers.CategoriesSerializer(query, many=True)
        return Response(serializer.data, status=200)