# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product", sku="12345", quantity=50)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.quantity, 50)
