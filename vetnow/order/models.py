import uuid
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.timezone import now
from product.models import Product

User = settings.AUTH_USER_MODEL


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
    confirmation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{str(self.owner)}'


@receiver(pre_save, sender=Order)
def set_amount(sender, instance, *args, **kwargs):
    # when we got peyment status p (payed) we set payment_date
    if instance.payment_status == 'p':
        instance.payment_date = now()

    # TODO if going to cancelled and ... what we do with amount


class RefundOrdersRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='refunds')
    order_id = models.TextField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    Confirmation = models.BooleanField(default=False)


@receiver(post_save, sender=RefundOrdersRequest)
def set_refund(sender, instance, *args, **kwargs):
    if instance.Confirmation == True:
        orderid = instance.order_id
        exists = Order.objects.filter(order_id=orderid)
        if exists:
            order = exists.first()
            order.payment_status = 'r'
            order.save()
    else:
        pass

