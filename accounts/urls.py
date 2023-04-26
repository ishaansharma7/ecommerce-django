from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_success_index, RegisterView, CustomLoginView


app_name = 'accounts_app'

urlpatterns = [
    path('test/', login_success_index, name='done_login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts_app:login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]