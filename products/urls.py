from django.urls import path
from .views import main_listing, product_detail, place_order, past_orders, search_bar
from django.views.generic import TemplateView


app_name = 'products_app'

urlpatterns = [
    path('all/', main_listing, name='main_listing'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),
    path('place-order/<int:pk>/', place_order, name='place_order'),
    path('purchased/', TemplateView.as_view(template_name='products/purchase_confirm.html'), name='purchased'),
    path('orders/', past_orders, name='past_orders'),
    path('search/', search_bar, name='search_bar'),

]