from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_success_index, RegisterView, CustomLoginView, after_login_redirect


app_name = 'accounts_app'

urlpatterns = [
    path('test/', login_success_index, name='done_login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='products_app:main_listing'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('redirecting/', after_login_redirect, name='al_redirect'),
]