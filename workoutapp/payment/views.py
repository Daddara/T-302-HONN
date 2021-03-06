import json
from json import JSONDecodeError

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from payment.models import Product, Order

# Create your views here.
from wallet.models import Wallet


@login_required
def purchase_fitcoins(request):
    #  User selects amount of fitcoin to purchase before clicking the overview button
    products = Product.objects.all().order_by('-fitcoins')
    return render(request, 'payment/shop_fitcoins.html', context={'products': products})


@login_required
def product_overview(request, product_id):
    #  Overview over selected fitcoin package
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'payment/product_overview.html', context={'product': product})


@login_required
def payment_validation(request):
    """This view is called via javascript method completeOrder in order_overview.html file after the payment has been
    processed in the paypal client. The purpose of this view is to check if all the payment data received from paypal is
    valid, and returns an appropriate response"""
    # If someone is trying to access the url without a json body
    try:
        body = json.loads(request.body)
    except JSONDecodeError:
        return render(request, '400.html', context={'error': 'Something unexplainable went wrong.'}, status=400)
    currency = str(body['currency'])
    amount = round(float(body['amount']), 2)

    # If someone tampered with currency
    if not currency == 'USD':
        print("currency invalid")
        return render(request, '400.html', context={'error': 'You have paid with the incorrect currency. Please'
                                                             'contact the administrators of the website via the '
                                                             'support page.'}, status=400)
    product_id = int(body['productID'])

    # Get product by id, return 404 if doesn't exist
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return render(request, '404.html', context={'error': 'No product with id ' + product_id + " exists."},
                      status=404)

    # If someone tampered with the price of the product
    if not float(amount) == float(product.price_usd()):
        print("amount invalid")
        return render(request, '400.html', context={'error': 'The price of the product was tampered with. The order'
                                                             'was canceled. Please contact support, or refund via '
                                                             'paypal.'}, status=400)

    # Everything checks out -> Create an order
    new_order = Order.objects.create(product=product, customer=request.user, price=product.price_usd())
    new_order.save()
    user = request.user  # Fetching user
    user_wallet = Wallet.objects.get(user=user)  # Fetching user wallet
    user_wallet.add_balance(product.fitcoins)  # Adding to user balance

    return JsonResponse({'orderID': new_order.id}, status=201)


@login_required
def payment_success(request, order_id):
    try:
        order = Order.objects.get(pk=order_id, customer=request.user)
    except Order.DoesNotExist:
        return render(request, '404.html', context={'error': 'Order does not exist'})

    return render(request, 'payment/complete.html', context={'order': order})


@login_required
def service_product_not_found(request, product_id):
    return render(request, '404.html', context={'error': 'No product with id ' + product_id + " exists."})


@login_required
def service_payment_invalid(request, invalid_id):
    # invalid 1 : Amount tampering
    if invalid_id == 1:
        return render(request, '400.html', context={'error': 'The price of the product was tampered with. The order'
                                                             'was canceled. Please contact support, or refund via '
                                                             'paypal.'})
    # invalid 2 : Currency tampering
    if invalid_id == 2:
        return render(request, '400.html', context={'error': 'You have paid with the incorrect currency. Please'
                                                             'contact the administrators of the website via the '
                                                             'support page.'})

    else:
        return render(request, '400.html', context={'error': 'Something unexplainable went wrong.'})


@login_required
def service_payment_validation(request, product_id, error_insertion):
    """This is the service stub for the payment system. It allows bypassing of paypal payments in order to test
    the functionality of the system. Instead of calling the payment_complete view when testing we call this view.
    The paypal integration is still available on the client side."""
    # For exception handling test
    if error_insertion != 0:
        return redirect('invalid-payment', invalid_id=error_insertion)

    # Get product by id, return 404 if doesn't exist
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return redirect('product-404')

    # Everything checks out -> Create an order
    new_order = Order.objects.create(product=product, customer=request.user, price=product.price_usd())
    new_order.save()
    user = request.user  # Fetching user
    user_wallet = Wallet.objects.get(user=user)  # Fetching user wallet
    user_wallet.add_balance(product.fitcoins)  # Adding to user balance

    # Get the order ID straight from this view and redirect to completion page
    order_id = new_order.id
    return redirect('payment-success', order_id=order_id)
