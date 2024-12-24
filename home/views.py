from django.shortcuts import render
from django.contrib.auth.views import LoginView
from datetime import datetime
from order.models import Order
from order.views import get_order_items

today = datetime.today()

year = today.year
month = today.month
day = today.day


def home(request):
    # Get all pending orders and delivery date is today
    orders = Order.objects.filter(
        status='Pending', delivery_date__year=year, delivery_date__month=month, delivery_date__day=day).all()

    for order in orders:
        order.order_items = get_order_items(order)

    # Group order_items by product name
    product_items = {}
    for order in orders:
        for item in order.order_items:
            if item.raw_name in product_items:
                product_items[item.raw_name]['quantity'] += item.product.mass * item.quantity
            else:
                product_items[item.raw_name] = {
                    'quantity': item.product.mass * item.quantity,
                    'stock_quantity': item.stock_quantity}
            product_items[item.raw_name]['stock_status'] = 'Ok' if product_items[item.raw_name][
                'quantity'] <= product_items[item.raw_name]['stock_quantity'] else 'Out  of Stock'

    return render(request, 'index.html', {'product_items': product_items})


class UserLoginView(LoginView):
    template_name = 'home/login.html'
    redirect_authenticated_user = True
    extra_context = {'title': 'Login'}
