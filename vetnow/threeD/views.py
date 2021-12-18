from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product
from .models import ThreeD
from .serializers import ThreeDImagesSerializer


class ThreedViews(APIView):
    def get(self, request, slug):
        product = Product.objects.is_exist_product(slug)
        try:
            threed_images = ThreeD.objects.filter(product=product).first()
            serializer = ThreeDImagesSerializer(threed_images, context={'request': request})
        except:
            return Response({"1": "2"}, status=404)
        else:
            return Response(serializer.data, status=200)
