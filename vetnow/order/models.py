import uuid
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.timezone import now
from product.models import Product
from config import secret
from kavenegar import *

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
    order_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return f'{str(self.owner)}'

    class Meta:
        ordering = ['-id']


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item')
    price = models.PositiveBigIntegerField()
    c_price = models.PositiveBigIntegerField(null=True,blank=True)
    total_c_price = models.PositiveBigIntegerField(null=True,blank=True)
    quantity = models.PositiveIntegerField()
    total_amount = models.PositiveBigIntegerField(null=True, blank=True)
    order_id = models.UUIDField()
    created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.c_price = self.product.company_price
        self.total_c_price = self.product.company_price * self.quantity
        self.total_amount = self.price * self.quantity
        super(OrderItems, self).save(*args, **kwargs)


@receiver(pre_save, sender=Order)
def set_amount(sender, instance, *args, **kwargs):
    # when we got peyment status p (payed) we set payment_date
    if instance.payment_status == 'p':
        instance.payment_date = now()

    # TODO if going to cancelled and ... what we do with amount


@receiver(post_save, sender=Order)
def set_amount(sender, instance, *args, **kwargs):
    try:
        api = KavenegarAPI(secret.K_API_KEY)
        msg = str(instance.order_id)
        params = {
            'receptor': instance.owner.username,
            'template': 'vetnowaftershop',
            'token': msg,
            'type': 'sms',
        }   
        response = api.verify_lookup(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


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


@receiver(post_save, sender=OrderItems)
def set_quntity(sender, instance, *args, **kwargs):
    """
    this method
    If they buy products from the threat of buying
    that product, the total number in the warehouse will be reduced
    """
    value_of_product = instance.product.quantity
    value_of_product -= instance.quantity
    if value_of_product >= 0:
        instance.product.quantity = value_of_product
        instance.product.save()
    elif value_of_product < 0:
        instance.product.quantity = 0
        instance.product.save()
    
