from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('add', views.add_order, name='add_order'),
    path('<int:order_id>/edit',
         views.edit_order, name='edit_order'),
    path('<int:order_id>/remove',
         views.remove_order, name='remove_order'),
]
