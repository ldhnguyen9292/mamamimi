# -*- coding: utf-8 -*-

from django.db.models import Q
from ..models import Product


def get_products(query=None):
    """Return products based on the given query (name or SKU)."""
    regex = r'^[DR]\d{2}'

    if query:
        # Search by name or SKU
        products = Product.objects.filter(
            sku__iregex=regex
        ).filter(
            Q(name__icontains=query) | Q(sku__icontains=query)
        )
    else:
        # Get all products starting with Dxx or Rxx
        products = Product.objects.filter(sku__iregex=regex)

    return products


def get_products_by_category(products):
    """Return products grouped by category."""
    return [{'category': category, 'products': products.filter(category=category)} for category in ['meat', 'vegetable']]
