from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Category, Product
from order.models import Order
from django.db.models import Sum


class ComputeGain(APIView):
    """
    this class 
    get category by slug and find all product with this category in order then:
    compute all company_price and amount and assing to total prices and use (total_price - total_comapny_price)
    and send to front_end
    """

    def get(self, request, slug):
        category = Category.objects.filter(slug=slug)
        if category:
            category = category.first()
        else:
            return Response(status=404)

        products = category.products.all()
        orders = []
        total_amount = 0
        total_company_price = 0
        for p in products:
            orders += p.orders_p.filter(payment_status='p')
        for order in orders:
            total_amount += order.amount
            total_company_price += (order.product.all().aggregate(Sum('company_price'))).get('company_price__sum')
        print(total_company_price)
        print(total_amount)
        gain_ = total_amount - total_company_price
        return Response({"gains": gain_}, status=200)
