from rest_framework import serializers
from .models import Category


class CategoriesSerializer(serializers.ModelSerializer):

    parent = serializers.SerializerMethodField(
        read_only=True, method_name="get_child_categories")

    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'parent',
        ]

    def get_child_categories(self, obj):
        """ self referral field """
        serializer = CategoriesSerializer(
            instance=obj.children.all(),
            many=True
        )
        return serializer.data
