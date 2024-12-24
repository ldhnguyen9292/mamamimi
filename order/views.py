from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm, OrderItemFormSet


def get_order_items(order):
    order_items = order.items.all()
    for item in order_items:
        item.stock_status = 'Out of Stock'
        set_products = item.product.set_products.all()
        for set_product in set_products:
            if item.quantity * item.product.mass <= set_product.quantity:
                item.stock_status = 'Ok'
            item.stock_quantity = set_product.quantity
            item.raw_name = set_product.name
    return order_items


def order_list(request):
    orders = Order.objects.all().order_by('-delivery_date')
    for order in orders:
        order.order_items = get_order_items(order)
    return render(request, 'order/order_list.html', {'orders': orders})


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            order = form.save()
            items = formset.save(commit=False)
            for item in items:
                item.order = order
                item.save()
            return redirect('/orders/')
    else:
        form = OrderForm()
        formset = OrderItemFormSet()
    return render(request, 'order/order_form.html', {'form': form, 'formset': formset})


def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, instance=order)
        if form.is_valid() and formset.is_valid():
            order = form.save()
            # Save the formset with the order instance
            items = formset.save(commit=False)
            for item in items:
                item.order = order
                item.save()
            return redirect('/orders/')
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(instance=order)
    return render(request, 'order/order_form.html', {'form': form, 'formset': formset})


def remove_order(_request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('/orders/')
