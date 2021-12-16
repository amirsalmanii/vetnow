from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now

User = get_user_model()


class Order(models.Model):
    PAYMENT_STATUS = (
        ("p", "payed"),
        ("c", "cancelled"),
        ("w", "pending"),  # w --> waited
        ("r", "refund")
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(Product, related_name='order_detail')
    amount = models.BigIntegerField(null=True, blank=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=20)
    payment_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.owner)}'

    # note we use display decorator in admin.py, and we don't use that
    # def get_products(self):
    #     """
    #     send list of products to admin panel
    #     """
    #     products = self.product.all()
    #     list_of_pr_names = []
    #     for p in products:
    #          list_of_pr_names.append(p.name)
    #     return list_of_pr_names


@receiver(pre_save, sender=Order)
def set_amount(sender, instance, *args, **kwargs):
    """
    this comments when we implement cart in backend
    needed but now cart in front end
    """
    # products = instance.product.all()
    # total_amount = 0
    # for p in products:
    #     total_amount += p.price
    # instance.amount = total_amount

    # when we got peyment status p (payed) we set payment_date
    if instance.payment_status == 'p':
        instance.payment_date = now()

    # TODO if going to cancelled and ... what we do with amount
