from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore



# Create your views here.
def main_listing(request):
    products = Product.objects.all()
    context = {'product_list': products}
    session = request.session
    session['last_page_visited'] = request.build_absolute_uri()
    print(session['last_page_visited'])
    return render(request, 'products/main_listing.html', context=context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'item': product}
    session = request.session
    session['last_page_visited'] = request.build_absolute_uri()
    print(session['last_page_visited'])
    return render(request, 'products/product_detail.html', context=context)


def place_order(request, pk):
    user = request.user
    if request.user.is_authenticated:
        user = request.user
        product = Product.objects.get(pk=pk)
        order = Order.objects.create(product=product, ordered_by=user)
        return HttpResponse('order placed successfully')
    else:
        return redirect('accounts_app:login')