from django.urls import path
from .views import main_listing, product_detail


app_name = 'products_app'

urlpatterns = [
    path('all', main_listing, name='main_listing'),
    path('detail/<int:pk>', product_detail, name='product_detail'),

]