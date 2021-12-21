from django.contrib import admin
from django.contrib.admin import display

from .models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "get_Category_child")
    search_fields = ("name",)

    @display(ordering='', description='child')
    def get_Category_child(self, obj):
        return obj.parent


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "available", "price", "quantity", "like_count")
    list_editable = ("available", "price", "quantity")
    list_filter = ("available", "price")
    search_fields = ("name", "descreption")
