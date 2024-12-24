# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from .services.product_services import get_products, get_products_by_category
from .forms import ProductForm
from .models import Product
from .models import Product
from .models import Notification


@login_required(login_url='/')
def inventory_list(request):
    """Display list of products."""
    products = get_products()
    data = get_products_by_category(products)

    return render(request, 'inventory/inventory_list.html', {'data': data})


@login_required(login_url='/')
def inventory_search(request):
    """Search products by name or SKU."""
    query = request.GET.get('q', '')
    products = get_products(query)
    data = get_products_by_category(products)

    return render(request, 'inventory/inventory_list.html', {'data': data, 'query': query})


@login_required(login_url='/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = ProductForm()

    return render(request, 'inventory/product_form.html', {'form': form})


@login_required(login_url='/')
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'inventory/product_form.html', {'form': form})


@login_required(login_url='/')
@csrf_exempt  # Alternatively, use built-in CSRF middleware in templates
def update_product(request):
    if request.method == "POST":
        sku = request.POST.get("sku")
        quantity = request.POST.get("quantity")

        if not sku or quantity is None:
            return HttpResponseBadRequest("Invalid input")

        try:
            quantity = float(quantity)
            product = Product.objects.get(sku=sku)
            product.quantity = quantity
            product.save()
        except Product.DoesNotExist:
            return HttpResponseBadRequest("Product not found")
        except ValueError:
            return HttpResponseBadRequest("Invalid quantity value")

    return redirect("inventory_list")  # Redirect to the inventory page


@login_required(login_url='/')
def notifications(request):
    notifications = Notification.objects.filter(read=False)
    return render(request, 'inventory/notifications.html', {'notifications': notifications})
