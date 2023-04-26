from django.shortcuts import render
from .models import Product


# Create your views here.
def main_listing(request):
    products = Product.objects.all()
    context = {'product_list': products}
    return render(request, 'products/main_listing.html', context=context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'item': product}
    return render(request, 'products/product_detail.html', context=context)