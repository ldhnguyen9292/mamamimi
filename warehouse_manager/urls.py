from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('orders/', include('order.urls')),
]
