from django.db import models


class ProductExistManager(models.Manager):
    """
    check this product with this slug is available or not
    """
    def is_exist_product(self, slug):
        product = self.model.objects.filter(slug=slug)
        if product:
            return product.first()
        else:
            return False