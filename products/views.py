from django.shortcuts import render, redirect
from .models import Product, Order
from accounts.models import AllUsers
from django.contrib.auth.decorators import login_required
from django.db.models import Q



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


@login_required
def place_order(request, pk):
    user = request.user
    if request.user.is_authenticated:
        user = request.user
        product = Product.objects.get(pk=pk)
        order = Order.objects.create(product=product, ordered_by=user)
        return redirect('products_app:purchased')
    else:
        return redirect('accounts_app:login')


@login_required
def past_orders(request):
    user = request.user
    user_details = AllUsers.objects.prefetch_related('order_set').get(id=user.id)
    old_orders = list(user_details.order_set.all().order_by('-order_date'))
    context = {'item': user_details, 'past_orders': old_orders}
    return render(request, 'products/orders.html', context=context)


def search_bar(request):
    search_text = request.GET.get('search_bar')
    products = Product.objects.filter(Q(name__icontains=search_text)| Q(details__icontains=search_text))
    context = {'product_list': products}
    session = request.session
    session['last_page_visited'] = request.build_absolute_uri()
    print(session['last_page_visited'])
    return render(request, 'products/main_listing.html', context=context)