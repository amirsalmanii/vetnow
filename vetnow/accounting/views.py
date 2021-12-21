from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Category, Product


class ComputeGain(APIView):
    def get(self, request, slug):
        category = Category.objects.filter(slug=slug)
        if category:
            category = category.first()
        else:
            return Response(status=404)

        products = category.products.all()
        company_price = 0
        price = 0
        for p in products:
            price += p.price
            company_price += p.company_price
        gains_ = price - company_price
        return Response({"gains": gains_}, status=200)
