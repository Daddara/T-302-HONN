from django.urls import path
from . import views

urlpatterns = [
    path('shop-fitcoins/', views.purchase_fitcoins, name='purchase-fitcoins'),
    path('product-overview/<int:product_id>/', views.product_overview, name="overview"),
    path('validate-payment/', views.payment_validation, name="validate-payment"),
    path('payment-success/<int:order_id>/', views.payment_success, name="payment-success"),
    path('test-product-404/<int:product_id>/', views.service_product_not_found, name="product-404"),
    path('test-invalid-payment/<int:invalid_id>/', views.service_payment_invalid, name="invalid-payment"),
    path('test-payment-confirmation/<int:product_id>/<int:error_insertion>/', views.service_payment_complete, name='test-payment')
]