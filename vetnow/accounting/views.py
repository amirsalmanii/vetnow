import datetime
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
        # print(total_company_price)
        # print(total_amount)
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
            data_start = data_start.split('-')
            data_end = serializer.validated_data.get('date_end')
            data_end = data_end.split('-')

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
        return Response({"gains": gain_, "total_sells_per_month": total_amount}, status=200)


class ComputeGainPerMonthAutoView(APIView):

    def get(self, request):
        esf_end_day = 29
        leap_year = datetime.datetime.now().year
        if (leap_year % 4) == 0:
            if (leap_year % 100) == 0:
                if (leap_year % 400) == 0:
                    esf_end_day = 30
                else:
                    pass
            else:
                esf_end_day = 30
        else:
            pass


        farvardin_s = jdatetime.date(1400, 1, 1).togregorian()
        farvardin_e = jdatetime.date(1400, 1, 31).togregorian()

        ordibehesht_s = jdatetime.date(1400, 2, 1).togregorian()
        ordibehesht_e = jdatetime.date(1400, 2, 31).togregorian()

        khordad_s = jdatetime.date(1400, 3, 1).togregorian()
        khordad_e = jdatetime.date(1400, 3, 31).togregorian()

        tir_s = jdatetime.date(1400, 4, 1).togregorian()
        tir_e = jdatetime.date(1400, 4, 31).togregorian()

        mordad_s = jdatetime.date(1400, 5, 1).togregorian()
        mordad_e = jdatetime.date(1400, 5, 31).togregorian()

        sharivar_s = jdatetime.date(1400, 6, 1).togregorian()
        sharivar_e = jdatetime.date(1400, 6, 31).togregorian()

        mehr_s = jdatetime.date(1400, 7, 1).togregorian()
        mehr_e = jdatetime.date(1400, 7, 30).togregorian()

        aban_s = jdatetime.date(1400, 8, 1).togregorian()
        aban_e = jdatetime.date(1400, 8, 30).togregorian()

        azar_s = jdatetime.date(1400, 9, 1).togregorian()
        azar_e = jdatetime.date(1400, 9, 30).togregorian()

        dey_s = jdatetime.date(1400, 10, 1).togregorian()
        dey_e = jdatetime.date(1400, 10, 30).togregorian()

        bahman_s = jdatetime.date(1400, 11, 1).togregorian()
        bahman_e = jdatetime.date(1400, 11, 30).togregorian()

        esfand_s = jdatetime.date(1400, 12, 1).togregorian()
        esfand_e = jdatetime.date(1400, 12, esf_end_day).togregorian()


        farvardin = Order.objects.filter(payment_status='p', created__gte=farvardin_s, created__lte=farvardin_e).aggregate(Sum('amount'))

        ordibehesht = Order.objects.filter(payment_status='p', created__gte=ordibehesht_s, created__lte=ordibehesht_e).aggregate(Sum('amount'))

        khordad = Order.objects.filter(payment_status='p', created__gte=khordad_s, created__lte=khordad_e).aggregate(Sum('amount'))

        tir = Order.objects.filter(payment_status='p', created__gte=tir_s, created__lte=tir_e).aggregate(Sum('amount'))

        mordad = Order.objects.filter(payment_status='p', created__gte=mordad_s, created__lte=mordad_e).aggregate(Sum('amount'))

        sharivar = Order.objects.filter(payment_status='p', created__gte=sharivar_s, created__lte=sharivar_e).aggregate(Sum('amount'))

        mehr = Order.objects.filter(payment_status='p', created__gte=mehr_s, created__lte=mehr_e).aggregate(Sum('amount'))

        aban = Order.objects.filter(payment_status='p', created__gte=aban_s, created__lte=aban_e).aggregate(Sum('amount'))

        azar = Order.objects.filter(payment_status='p', created__gte=azar_s, created__lte=azar_e).aggregate(Sum('amount'))

        dey = Order.objects.filter(payment_status='p', created__gte=dey_s, created__lte=dey_e).aggregate(Sum('amount'))

        bahman = Order.objects.filter(payment_status='p', created__gte=bahman_s, created__lte=bahman_e).aggregate(Sum('amount'))

        esfand = Order.objects.filter(payment_status='p', created__gte=esfand_s, created__lte=esfand_e).aggregate(Sum('amount'))


        return Response({
            "farvardin": farvardin,
            "ordibehesht": ordibehesht,
            "khordad": khordad,
            "tir": tir,
            "mordad": mordad,
            "sharivar": sharivar,
            "mehr": mehr,
            "aban": aban,
            "azar": azar,
            "dey": dey,
            "bahman": bahman,
            "esfand": esfand
            }, status=200)


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
        # send total gain and send total amounts(total sells)
        return Response({"total_gain": result, "total_sells": total_amounts_of_orders}, status=200)



