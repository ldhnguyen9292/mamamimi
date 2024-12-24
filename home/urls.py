from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from order.views import order_list
from inventory.views import inventory_list

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
