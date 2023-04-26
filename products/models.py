from django.db import models
from accounts.models import AllUsers
from django.utils.text import slugify


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    img_link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    ordered_by = models.ForeignKey(AllUsers, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.name