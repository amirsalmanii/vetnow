from django.contrib import admin
from django.contrib.admin import display
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "get_Category_child")
    search_fields = ("name",)

    @display(ordering='', description='child')
    def get_Category_child(self, obj):
        return obj.parent


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "available", "price", "company_price","quantity")
    list_editable = ("available", "price", "company_price", "quantity")
    list_filter = ("available", "price")
    search_fields = ("name", "descreption")
