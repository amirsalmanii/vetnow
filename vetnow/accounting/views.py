from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Category, Product
from order.models import Order
from django.db.models import Sum
from .serializers import DateSerilizer
import jdatetime
from datetime import date


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


class ComputeGainWithTime(APIView):
    """
    Like above class just we show gains with date
    this class 
    get category by slug and find all product with this category in order then:
    compute all company_price and amount and assing to total prices and use (total_price - total_comapny_price)
    and send to front_end
    """

    def post(self, request):
        serializer = DateSerilizer(data=request.data)
        if serializer.is_valid():
            # change miladi to shamsi for filtering
            slug = serializer.validated_data.get('slug')
            data_start = serializer.validated_data.get('date_start')
            data_start = data_start.split(' ')
            data_end = serializer.validated_data.get('date_end')
            data_end = data_end.split(' ')

            data_start = [int(times) for times in data_start]
            data_end = [int(times) for times in data_end]
        else:
            return Response(serializer.errors, status=400)


        date_start = (jdatetime.date(data_start[0], data_start[1], data_start[2]).togregorian())
        date_end = jdatetime.date(data_end[0], data_end[1], data_end[2]).togregorian()


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
            orders += p.orders_p.filter(payment_status='p', payment_date__gte=(date(date_start.year,date_start.month,date_start.day)), payment_date__lte=(date(date_end.year, date_end.month, date_end.day)))
        for order in orders:
            total_amount += order.amount
            total_company_price += (order.product.all().aggregate(Sum('company_price'))).get('company_price__sum')
        gain_ = total_amount - total_company_price
        return Response({"gains": gain_}, status=200)


class AllOdersCountView(APIView):
    """
    return all orders count
    """
    def get(self, request):
        orders = Order.objects.filter(payment_status='p').count()
        return Response({"all": orders}, status=200)


class TotalCategoryGainsView(APIView):
    """
    find total orders amounts
    and find company price of orders products
    and subtracts these numbers
    """
    def get(self, request):
        total_amounts_of_orders = (Order.objects.filter(payment_status='p').aggregate(Sum('amount'))).get('amount__sum')

        # Addition products company price in orders
        products_in_orders = Order.objects.filter(payment_status='p')
        all_products_in_orders_company_price = 0
        for pr in products_in_orders:
            all_products_in_orders_company_price += (pr.product.all().aggregate(Sum('company_price'))).get('company_price__sum')


        result = total_amounts_of_orders - all_products_in_orders_company_price
        return Response({"total_gain":result},status=200)


