from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mark
from . import serializers


class ListMarkedProducts(APIView):
    def get(self, request):
        marks = Mark.objects.filter(user=request.user)
        serializer = serializers.MarkProductsSerializer(marks, many=True, context={'request': request})
        return Response(serializer.data, status=200)



