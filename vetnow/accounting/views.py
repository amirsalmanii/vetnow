import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Category, Product
from order.models import Order, OrderItems
from django.db.models import Sum
from .serializers import DateSerilizer
import jdatetime
from datetime import date


class ComputeGainPerMonthAutoView(APIView):
    """
    compute sells per month and send to frontend charts
    """

    def get(self, request):
        """
        to know this year is leap year or not
        """
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

        # for knowing we are in 1400 or 1401 and etc...
        date_to_ir_update = datetime.datetime.now()
        year_ = date_to_ir_update.year
        month_ = date_to_ir_update.month
        day_ = date_to_ir_update.day

        year_ = jdatetime.date.fromgregorian(year=year_, month=month_, day=day_).year
        farvardin_s = jdatetime.date(year_, 1, 1).togregorian()
        farvardin_e = jdatetime.date(year_, 1, 31).togregorian()

        ordibehesht_s = jdatetime.date(year_, 2, 1).togregorian()
        ordibehesht_e = jdatetime.date(year_, 2, 31).togregorian()

        khordad_s = jdatetime.date(year_, 3, 1).togregorian()
        khordad_e = jdatetime.date(year_, 3, 31).togregorian()

        tir_s = jdatetime.date(year_, 4, 1).togregorian()
        tir_e = jdatetime.date(year_, 4, 31).togregorian()

        mordad_s = jdatetime.date(year_, 5, 1).togregorian()
        mordad_e = jdatetime.date(year_, 5, 31).togregorian()

        sharivar_s = jdatetime.date(year_, 6, 1).togregorian()
        sharivar_e = jdatetime.date(year_, 6, 31).togregorian()

        mehr_s = jdatetime.date(year_, 7, 1).togregorian()
        mehr_e = jdatetime.date(year_, 7, 30).togregorian()

        aban_s = jdatetime.date(year_, 8, 1).togregorian()
        aban_e = jdatetime.date(year_, 8, 30).togregorian()

        azar_s = jdatetime.date(year_, 9, 1).togregorian()
        azar_e = jdatetime.date(year_, 9, 30).togregorian()

        dey_s = jdatetime.date(year_, 10, 1).togregorian()
        dey_e = jdatetime.date(year_, 10, 30).togregorian()

        bahman_s = jdatetime.date(year_, 11, 1).togregorian()
        bahman_e = jdatetime.date(year_, 11, 30).togregorian()

        esfand_s = jdatetime.date(year_, 12, 1).togregorian()
        esfand_e = jdatetime.date(year_, 12, esf_end_day).togregorian()

        farvardin = Order.objects.filter(
            payment_status="p", created__gte=farvardin_s, created__lte=farvardin_e
        ).aggregate(Sum("amount"))

        ordibehesht = Order.objects.filter(
            payment_status="p", created__gte=ordibehesht_s, created__lte=ordibehesht_e
        ).aggregate(Sum("amount"))

        khordad = Order.objects.filter(
            payment_status="p", created__gte=khordad_s, created__lte=khordad_e
        ).aggregate(Sum("amount"))

        tir = Order.objects.filter(
            payment_status="p", created__gte=tir_s, created__lte=tir_e
        ).aggregate(Sum("amount"))

        mordad = Order.objects.filter(
            payment_status="p", created__gte=mordad_s, created__lte=mordad_e
        ).aggregate(Sum("amount"))

        sharivar = Order.objects.filter(
            payment_status="p", created__gte=sharivar_s, created__lte=sharivar_e
        ).aggregate(Sum("amount"))

        mehr = Order.objects.filter(
            payment_status="p", created__gte=mehr_s, created__lte=mehr_e
        ).aggregate(Sum("amount"))

        aban = Order.objects.filter(
            payment_status="p", created__gte=aban_s, created__lte=aban_e
        ).aggregate(Sum("amount"))

        azar = Order.objects.filter(
            payment_status="p", created__gte=azar_s, created__lte=azar_e
        ).aggregate(Sum("amount"))

        dey = Order.objects.filter(
            payment_status="p", created__gte=dey_s, created__lte=dey_e
        ).aggregate(Sum("amount"))

        bahman = Order.objects.filter(
            payment_status="p", created__gte=bahman_s, created__lte=bahman_e
        ).aggregate(Sum("amount"))

        esfand = Order.objects.filter(
            payment_status="p", created__gte=esfand_s, created__lte=esfand_e
        ).aggregate(Sum("amount"))

        return Response(
            {
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
            },
            status=200,
        )  # TODO change this datas this is just for test


class AllOdersCountView(APIView):
    """
    return all orders count
    """

    def get(self, request):
        orders = Order.objects.filter(payment_status="p").count()
        return Response({"all": orders}, status=200)


class ComputeGain(APIView):
    """
    compute gains with filtering category
    """

    def get(self, request, slug):
        category = Category.objects.filter(slug=slug)
        if category:
            category = category.first()
        else:
            return Response(status=404)

        orders_item = OrderItems.objects.filter(product__categories=category)
        total_f = orders_item.aggregate(Sum("total_amount"))["total_amount__sum"] # total sells
        total_c = orders_item.aggregate(Sum("total_c_price"))["total_c_price__sum"] # total company price per product in orders item
        try:
            result = total_f - total_c
        except:
            result = 0
        return Response({"gains": result}, status=200)


class ComputeGainWithTime(APIView):
    """
    compute gains and sells per entered dates with filtering category
    """

    def post(self, request):
        serializer = DateSerilizer(data=request.data)
        if serializer.is_valid():
            # change miladi to shamsi for filtering
            slug = serializer.validated_data.get("slug")
            data_start = serializer.validated_data.get("date_start")
            data_start = data_start.split("-")
            data_end = serializer.validated_data.get("date_end")
            data_end = data_end.split("-")

            data_start = [int(times) for times in data_start]
            data_end = [int(times) for times in data_end]
        else:
            return Response(serializer.errors, status=400)

        date_start = jdatetime.date(
            data_start[0], data_start[1], data_start[2]
        ).togregorian()
        date_end = jdatetime.date(data_end[0], data_end[1], data_end[2]).togregorian()

        category = Category.objects.filter(slug=slug)
        if category:
            category = category.first()
        else:
            return Response(status=404)

        orders_item = OrderItems.objects.filter(
            product__categories=category,
            created__gte=(date(date_start.year, date_start.month, date_start.day)),
            created__lte=(date(date_end.year, date_end.month, date_end.day)),
        )

        total_f = orders_item.aggregate(Sum("total_amount"))["total_amount__sum"]
        total_c = orders_item.aggregate(Sum("total_c_price"))["total_c_price__sum"]
        try:
            result = total_f - total_c
        except:
            result = 0
        return Response({"gains": result, "total_sells_per_month": total_f}, status=200)


class TotalCategoryGainsView(APIView):
    """
    compute total gains in all categories
    """

    def get(self, request):
        orders_item = OrderItems.objects.all()
        total_f = orders_item.aggregate(Sum("total_amount"))["total_amount__sum"]
        total_c = orders_item.aggregate(Sum("total_c_price"))["total_c_price__sum"]

        try:
            result = total_f - total_c
        except:
            result = 0
        return Response({"total_gain": result, "total_sells": total_f}, status=200)
