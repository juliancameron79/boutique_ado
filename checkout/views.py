from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(revrse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H8ZaxHCNCnqhPAa9y8ilQdgLSVXwZgI6UhWTwygmUSbl8G3ZGygHT2h1jKGRRKV5kiOBBi5Zaj21YwIfSArX4dQ00YWGgMSKj',
        'client_secret': 'test client secret',
    }

    return render(request,template, context)
