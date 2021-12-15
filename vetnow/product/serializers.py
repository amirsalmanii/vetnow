from rest_framework import serializers
from .models import Category, Product


class CategoriesSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField(
        read_only=True, method_name="get_child_categories")

    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'get_absolute_url',
            'parent',
        ]

    def get_child_categories(self, obj):
        """ self referral field """
        serializer = CategoriesSerializer(
            instance=obj.children.all(),
            many=True
        )
        return serializer.data


class CategoryProductSerializer(serializers.ModelSerializer):
    """
    for give to product serializer field categories
    """
    class Meta:
        model = Category
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    categories = CategoryProductSerializer(many=True)

    class Meta:
        model = Product
        fields = ('name',
                  'slug',
                  'thumbnail',
                  'image',
                  'get_absolute_url',
                  'descreption',
                  'price',
                  'quantity',
                  'like',
                  'like_count',
                  'categories'
                  )
