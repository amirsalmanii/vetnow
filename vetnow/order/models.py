from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from django.db.models.signals import pre_save, post_save
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
    product = models.ManyToManyField(Product, related_name='orders_p')
    amount = models.BigIntegerField(null=True, blank=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=20)
    payment_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.owner)}'


@receiver(pre_save, sender=Order)
def set_amount(sender, instance, *args, **kwargs):
    # when we got peyment status p (payed) we set payment_date
    if instance.payment_status == 'p':
        instance.payment_date = now()

    # TODO if going to cancelled and ... what we do with amount
