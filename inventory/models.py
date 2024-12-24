# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    CATEGORY_STATUS = [('vegetable', 'vegetable'),
                       ('meat', 'meat'), ('set', 'set')]
    LOCATION_DEFAULT = [('Nha Nguyen', 'Nha Nguyen'), ('Nha Hang', 'Nha Hang')]
    UNIT_DEFAULT = [('g', 'g'), ('con', 'con'), ('ml', 'ml')]

    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    category = models.CharField(
        max_length=50, choices=CATEGORY_STATUS, default='vegetable')
    mass = models.FloatField(default=0)
    unit = models.CharField(max_length=50, choices=UNIT_DEFAULT, default='g')
    quantity = models.FloatField(default=0)
    note = models.TextField(blank=True)
    location = models.CharField(
        max_length=255, choices=LOCATION_DEFAULT, default='Nha Nguyen')
    set_products = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.category == 'set':
            components = ', '.join(
                [f"{product.name} with sku - {product.sku}" for product in self.set_products.all()])
            return f"{self.name}: {components}"
        return self.name


class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message


@receiver(post_save, sender=Product)
def check_low_stock(sender, instance, **kwargs):
    if instance.quantity < 1:
        Notification.objects.create(message=f"Low stock for {instance.name}")
