from django.db import models
from django.db.models.signals import post_save, pre_save, m2m_changed, pre_delete
from django.dispatch import receiver
from product.models import Product
import jdatetime


class Discount(models.Model):
    products = models.ManyToManyField(Product, related_name='pdiscount')
    discount_percent = models.FloatField(null=True, blank=True, default=0)
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)


# this is when first time created obj
@receiver(m2m_changed, sender=Discount.products.through)
def update_discount_price_in_products(sender, instance, action, reverse, *args,  **kwargs):
    if action == 'post_add':
        products = instance.products.all()
        percent = instance.discount_percent
        for pr in products:
            pr.price_after_discount = pr.price - (1 / 100) * percent * pr.price
            pr.save()


# when save instance we convert shamsi to milady
@receiver(pre_save, sender=Discount)
def update_date(sender, instance, *args, **kwargs):
    date_from = instance.valid_from
    date_to = instance.valid_to
    valid_from_ = jdatetime.date(year=date_from.year, month=date_from.month, day=date_from.day).togregorian()
    valid_to_ = jdatetime.date(year=date_to.year, month=date_to.month, day=date_to.day).togregorian()

    instance.valid_from = valid_from_
    instance.valid_to = valid_to_

# this is when updated obj
@receiver(post_save, sender=Discount)
def update_discount_price_in_products(sender, instance, *args,  **kwargs):
    products = instance.products.all()
    percent = instance.discount_percent
    for pr in products:
        pr.price_after_discount = pr.price - (1 / 100) * percent * pr.price
        pr.save()
  # TODO what we can if active false


@receiver(pre_delete, sender=Discount)
def update_discount_price_in_products(sender, instance, *args,  **kwargs):
    products = instance.products.all()
    for pr in products:
        pr.price_after_discount = 0
        pr.save()


