from rest_framework import serializers
from .models import ThreeD
from order.serializers import ProductSerilizer


class ThreeDImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThreeD
        fields = '__all__'
