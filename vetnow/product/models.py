from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    descreption = models.TextField()
    price = models.BigIntegerField(default=0)
    quantity = models.BigIntegerField(default=0)
    like = models.BigIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name
