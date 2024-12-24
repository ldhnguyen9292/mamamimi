# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Notification


class ProductAdmin(admin.ModelAdmin):
    def get_set_products(self, obj):
        if obj.set_products.exists():  # Check if there are related products
            return ", ".join([p.name for p in obj.set_products.all()])
        return ""

    # Change the column name in the admin display
    get_set_products.short_description = "Set Products"

    list_display = ('name', 'sku', 'mass', 'unit', 'quantity',
                    'get_set_products', 'note')
    list_filter = ('category', 'unit')
    search_fields = ('name', 'sku')


admin.site.register(Product, ProductAdmin)
admin.site.register(Notification)
