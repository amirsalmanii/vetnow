from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:10]
