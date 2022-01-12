from django.db import models
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from product.models import Product


class Discount(models.Model):
    products = models.ManyToManyField(Product, related_name='pdiscount')
    discount_percent = models.FloatField(null=True, blank=True, default=0)
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


# this is when first time created obj
@receiver(m2m_changed, sender=Discount.products.through)
def update_discount_price_in_products(sender, instance, action, reverse, *args,  **kwargs):
    if action == 'post_add':
        products = instance.products.all()
        percent = instance.discount_percent
        for pr in products:
            pr.price_after_discount = pr.price - (1 / 100) * percent * pr.price
            pr.save()


# this is when updated obj
@receiver(post_save, sender=Discount)
def update_discount_price_in_products(sender, instance, *args,  **kwargs):
    products = instance.products.all()
    percent = instance.discount_percent
    for pr in products:
        pr.price_after_discount = pr.price - (1 / 100) * percent * pr.price
        pr.save()

  # TODO what we can if active false