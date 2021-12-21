from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product
from .models import ThreeD
from .serializers import ThreeDImagesSerializer, ThreeDImagesUpdateSerializer


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


class ThreedUpdate(APIView):
    def put(self, request, slug):
        product = Product.objects.is_exist_product(slug)
        try:
            threed_images = ThreeD.objects.filter(product=product).first()
            serializer = ThreeDImagesUpdateSerializer(instance=threed_images, data=request.data)
        except:
            return Response({"1": "2"}, status=404)
        else:
            # serializer.data['product'] = product
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors)


