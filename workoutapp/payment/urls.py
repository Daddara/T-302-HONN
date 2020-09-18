from django.urls import path
from . import views

urlpatterns = [
    path('shop-fitcoins/', views.purchase_fitcoins, name='purchase-fitcoins'),
    path('overview/<int:product_id>/', views.product_overview, name="overview"),
    path('payment-confirmation/', views.payment_complete, name="validate-payment"),
    path('order-complete/<int:order_id>/', views.completion_page, name="payment-success"),
    path('product-404/<int:product_id>/', views.product_not_found, name="product-404"),
    path('invalid-payment/<int:invalid_id>/', views.payment_invalid, name="invalid-payment"),
    path('test-payment-confirmation/<int:product_id>/<int:error_insertion>/', views.service_payment_complete, name='test-payment')
]