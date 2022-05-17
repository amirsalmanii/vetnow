from .models import Discount
from datetime import date


def my_scheduled_job():
    discounts = Discount.objects.all()
    for discount in discounts:
        if discount.valid_to < date.today():
            discount.delete()