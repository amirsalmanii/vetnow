from django.db import models


class ProductExistManager(models.Manager):
    def is_exist_product(self, slug):
        product = self.model.objects.filter(slug=slug)
        if product:
            return product.first()
        else:
            return False