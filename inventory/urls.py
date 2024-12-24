from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('search', views.inventory_search, name='inventory_search'),
    path('add', views.add_product, name='add_product'),
    path('<int:product_id>/edit',
         views.edit_product, name='edit_product'),
    path("update-product/", views.update_product, name="update_product"),
    path('notifications/', views.notifications, name='notifications'),
]
