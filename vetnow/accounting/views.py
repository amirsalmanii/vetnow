from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Category, Product
from django.db.models import Sum


class ComputeGain(APIView):
    def get(self, request, slug):
        category = Category.objects.filter(slug=slug)
        if category:
            category = category.first()
        else:
            return Response(status=404)

        products_price = category.products.all().aggregate(Sum('price'))
        products_company_price = category.products.all().aggregate(Sum('company_price'))
        print(products_price)
        gains_ = products_price['price__sum'] - products_company_price['company_price__sum']
        return Response({"gains": gains_}, status=200)
        