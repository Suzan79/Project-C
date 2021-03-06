from datetime import datetime
import requests

from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .models import Cart, Wish
from .forms import PayPalForm
from .functions import *
from products.models import Product, Design

def get_shopping_cart(request):
    '''
    This function checks if the user has a cart, if not, it creates one.
    Then when a product is added it calculates the total.
    '''
    cart = get_users_cart(request)

    if cart:
        new_total = 0.00
        for a in cart.item.all():
            new_total += float(a.product.price + a.art.artwork_price)
        cart.total = round(new_total, 2)
        cart.save()
        request.session['items_total'] = cart.item.count()
        payment_data = payment(request, cart, new_total)
        order = payment_data[0]
        form = payment_data[1]

        context = {"cart": cart, 'order': order, 'form': form}

    template = "carts/view.html"
    return render(request, template, context)


def add_delete_product(request, design_pk):
    '''
    This function adds or removes a product from the cart. Giving a notification when adding one.
    '''
    product = Design.objects.get(id=design_pk)

    cart = get_users_cart(request)

    if not product in cart.item.all():
        cart.item.add(product)
        request.session['items_total'] = cart.item.count()
        messages.success(request, "Item has been successfully added to your Shopping Cart.")
    else:
        cart.item.remove(product)
        request.session['items_total'] = cart.item.count()
        # messages.success(request, "This item is already in your shopping cart.")
        return HttpResponseRedirect(reverse("cart"))

    return JsonResponse({})


def payment(request, cart, total):
    '''
    This function returns the cart and the PayPal form (that will be sent to PayPal).
    You need to pass request, a cart and the total paid price for an order as parameters.
    '''
    host = request.get_host()

    paypal_form = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': total,
        'item_name': 'Order {}'.format(datetime.today()),
        'invoice': '',
        'currency_code': 'EUR',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }

    form = PayPalForm(initial=paypal_form)

    return cart, form
    

@csrf_exempt
def payment_done(request):
    messages.success(request, f'Payment succesful')
    return redirect('home_page')

@csrf_exempt
def payment_cancelled(request):
    messages.warning(request, f'Payment was cancelled')
    return redirect('cart')

@csrf_exempt
def request_to_paypal(request):
    '''
    This view calls a function that moves the products in the cart to the order history if the user has specified his/her address.
    It also sends a post request to PayPal.
    '''

    if check_address(request):
        date_time = move_to_orderhistory(request, get_users_cart(request))

        post_data = {
            'cmd' : request.POST.get("cmd",''),
            'charset' : request.POST.get("charset",''),
            'currency_code' : request.POST.get("currency_code",''),
            'no_shipping' : request.POST.get("no_shipping",''),
            'business' : request.POST.get("business",''),
            'amount' : request.POST.get("amount",''),
            'item_name' : request.POST.get("item_name",''),
            'invoice' : date_time,
            'notify_url' : request.POST.get("notify_url",''),
            'cancel_return' : request.POST.get("cancel_return",''),
            'return' : request.POST.get("return",''),
        }

        response = requests.post(get_endpoint(), data=post_data)

        return redirect(response.url)
    else:
        messages.warning(request, f'Please enter your address at your profile page before ordering.')
        return redirect('cart')
    
def get_wishlist(request):
    wishlist = get_users_wishlist(request)

    template = "carts/wishlist_view.html"
    context = {"wishlist": wishlist}

    return render(request, template, context)

def add_wish_item(request, design_pk):
    product = Design.objects.get(id=design_pk)

    wishlist = get_users_wishlist(request)

    if not product in wishlist.item.all():
        wishlist.item.add(product)
        messages.success(request, "Item has been successfully added to your Wish List.")
    else:
        messages.warning(request, "This item is already in your Wish List.")

    return JsonResponse({})
        
def delete_wish_item(request, design_pk):
    product = Design.objects.get(id=design_pk)

    wishlist = get_users_wishlist(request)

    if product in wishlist.item.all():
        wishlist.item.remove(product)

    messages.success(request, "Item has been deleted.")

    return HttpResponseRedirect(reverse("wishlist_page"))
