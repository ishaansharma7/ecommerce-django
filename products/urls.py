from django.urls import path
from .views import main_listing, product_detail, place_order
from django.views.generic import TemplateView


app_name = 'products_app'

urlpatterns = [
    path('all/', main_listing, name='main_listing'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),
    path('place-order/<int:pk>/', place_order, name='place_order'),
    path('purchased/', TemplateView.as_view(template_name='products/purchase_confirm.html'), name='purchased'),

]