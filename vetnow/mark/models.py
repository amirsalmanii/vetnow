from django.db import models
from django.conf import settings
from product.models import Product
User = settings.AUTH_USER_MODEL


class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marked')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='marked_products')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.user)} marked {self.product}'
