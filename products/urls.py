from django.urls import path
from .views import main_listing, product_detail, place_order


app_name = 'products_app'

urlpatterns = [
    path('all/', main_listing, name='main_listing'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),
    path('place-order/<int:pk>/', place_order, name='place_order'),

]