from rest_framework import serializers
from .models import Category, Product
from rest_framework.fields import CurrentUserDefault
from mark.models import Mark


class CategoriesSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField(
        read_only=True, method_name="get_child_categories")

    class Meta:
        model = Category
        fields = [
            'id',
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


class CategoryAddAndUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryProductSerializer(serializers.ModelSerializer):
    """
    for give to product serializer field categories
    """
    class Meta:
        model = Category
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    is_fav = serializers.SerializerMethodField()

    def get_is_fav(self, instance):
        """
        check this product fav of user or not
        if fav send true else send false
        """
        user = self.context.get('request').user
        try:
            Mark.objects.get(user=user, product=instance)
        except:
            return False
        else:
            return True
    
    categories = CategoryProductSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateSerializer(serializers.ModelSerializer):
    # categories = CategoryProductSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
