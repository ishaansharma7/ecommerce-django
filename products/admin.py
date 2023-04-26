from django.contrib import admin
from .models import ProductCategory, Product, Order

# Register your models here.
@admin.register(ProductCategory)
class AdminNewUser(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class AdminNewUser(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


@admin.register(Order)
class AdminNewUser(admin.ModelAdmin):
    list_display = ('product', 'ordered_by', 'order_date')