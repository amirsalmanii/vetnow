from django.contrib import admin
from .models import Order
from django.contrib.admin import display


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("owner", "get_all_products", "amount", "payment_status", "payment_date", "created_at", "order_id")
    list_editable = ("payment_status", )
    list_filter = ("created_at", "payment_status", "payment_date")
    search_fields = ("owner__username", "owner__first_name", "owner__last_name")

    @display(ordering='', description='products')
    def get_all_products(self, obj):
        """
        send list of products to admin panel
        """
        products = obj.product.all()
        list_of_pr_names = []
        for p in products:
             list_of_pr_names.append(p.name)
        return list_of_pr_names
