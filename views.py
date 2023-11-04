from decimal import Decimal

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order, User
from restaurant.models import Dish


@login_required
def order_now(request):
    # if request.method == 'POST':
    # selected_dish_ids = request.POST.getlist('selected_dish_ids')
    selected_dish_ids = request.session.get('cart', [])
    user_id = request.session.get('user_id')

    if user_id:
        user = User.objects.get(pk=user_id)
        order = Order.objects.create(user=user)
        order.dishes.add(*selected_dish_ids)
        request.session['cart'] = []
    return redirect('home')  # Redirect to the cart view or any other desired page


def add_to_cart(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    cart = request.session.get('cart', [])
    cart.append(dish.id)
    request.session['cart'] = cart
    return redirect('my_cart')


def my_cart(request):
    cart_item_ids = request.session.get('cart', [])
    cart_items = Dish.objects.filter(id__in=cart_item_ids)

    # Calculate the total price
    total = sum(item.price for item in cart_items)
    # Calculate the discount amount if total is above 2500
    discount_amount = Decimal(0)
    if total > Decimal(2000):
        discount_amount = total * Decimal(0.20)
        total -= discount_amount

    return render(request, 'my_cart.html', {
        'cart_items': cart_items,
        'total': total,
        'discount_amount': discount_amount,
    })


def my_orders(request):
    user_id = request.session.get('user_id')
    if user_id:
        user_orders = Order.objects.filter(user_id=user_id).order_by('-time_ordered')
    else:
        user_orders = None

    # Calculate the total price and apply discount for each order
    for order in user_orders:
        total_price = Decimal(0)
        for dish in order.dishes.all():
            total_price += dish.price


        # Apply a 20% discount if total price is above 2000
        if total_price > Decimal(2000):
            discount = total_price * Decimal(0.20)
            total_price -= discount
            order.discounted = True
            order.discount_amount = int(discount)
        else:
            order.discounted = False
            order.discount_amount = Decimal(0)

        order.total_price = int(total_price)

    return render(request, 'my_orders.html', {'user_orders': user_orders})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Order

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # Delete the order from the database
        order.delete()
        return redirect('my_orders')  # Redirect to the "my_orders" page or any other desired page

    return render(request, 'cancel_order_template.html', {'order': order})
