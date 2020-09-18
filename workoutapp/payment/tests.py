from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from payment.models import Product, Order
from wallet.models import Wallet


# Create your tests here.
class TestPayment(TestCase):
    def setUp(self):
        # Set up stuff before every test method
        # Initialize client
        self.client = Client()
        # Add product to database
        self.product = Product.objects.create(fitcoins=4000)

        # Create user
        data = {'username': 'TestUser',
                'email': 'test_user@test.com',
                'password1': 'iampassword', 'password2': 'iampassword'}
        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, '/accounts/login/', target_status_code=200)
        self.user = User.objects.get(pk=1)
        self.assertEqual(self.user.username, 'TestUser')
        self.client.login(username="TestUser", password="iampassword")

    def tearDown(self):
        # Clean up run after every test method.
        self.client.logout()

    def test_shop_fitcoins(self):
        """Testing the shop fitcoin page. The one containing all available products"""
        target_url = reverse('purchase-fitcoins')
        # Test server response to valid request
        print("Testing shop fitcoin page: ", end="")
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 200)
        print("200, OK")

        # Test server response to not logged in
        print("Testing shop fitcoin page: ", end="")
        self.client.logout()
        response = self.client.get(target_url)
        self.assert_login_redirect(next_page=target_url, response=response)
        print("401, OK")

    def test_product_overview(self):
        """Testing the single product overview. The one that contains the paypal checkout button"""
        # Test server response to valid product id
        print("Testing product overview page: ", end="")
        response = self.client.get(reverse('overview', kwargs={'product_id': self.product.id}), follow=True)
        self.assertEqual(response.status_code, 200)
        print("200, OK")

        # Test server response to incorrect product id
        print("Testing product overview page: ", end="")
        response = self.client.get(reverse('overview', kwargs={'product_id': 5}), follow=True)
        self.assertEqual(response.status_code, 404)
        print("404, OK")

        # Test server response to not logged in
        print("Testing product overview page: ", end="")
        self.client.logout()
        response = self.client.get(reverse('overview', kwargs={'product_id': self.product.id}))
        target_url = reverse('overview', kwargs={'product_id': self.product.id})
        self.assert_login_redirect(next_page=target_url, response=response)
        print("401, OK")

    def test_order_creation(self):
        print("Testing order creation: ", end="")
        product_id = self.product.id
        response = self.client.get(reverse('test-payment', kwargs={'product_id': product_id, 'error_insertion': 0}))
        try:
            order = Order.objects.get(pk=1)
            self.assertTrue(True)
        except Order.DoesNotExist:
            self.assertTrue(False)
        print("201, OK")

    def test_payment(self):
        print("Testing service payment: ", end="")
        product_id = self.product.id
        response = self.client.get(reverse('test-payment', kwargs={'product_id': product_id, 'error_insertion': 0}))
        order = Order.objects.get(pk=1)
        self.assertRedirects(response, reverse('payment-success', kwargs={'order_id': order.id}),
                             target_status_code=200)
        print("200, OK")

        print("Testing invalid payment 1: ", end="")
        response = self.client.get(reverse('test-payment', kwargs={'product_id': product_id, 'error_insertion': 1}))
        self.assertRedirects(response, reverse('invalid-payment', kwargs={'invalid_id': 1}), target_status_code=200)
        print("400, OK")

    def test_invalid_payment(self):
        product_id = self.product.id
        print("Testing order creation on invalid payment: ", end="")
        try:
            order = Order.objects.get(pk=1)
            self.assertTrue(False)
        except Order.DoesNotExist:
            self.assertTrue(True)
        print("204, OK")

        print("Testing invalid payment 2: ", end="")
        response = self.client.get(reverse('test-payment', kwargs={'product_id': product_id, 'error_insertion': 2}))
        self.assertRedirects(response, reverse('invalid-payment', kwargs={'invalid_id': 2}), target_status_code=200)
        print("400, OK")

        print("Testing invalid error id: ", end="")
        response = self.client.get(reverse('test-payment', kwargs={'product_id': product_id, 'error_insertion': 5}))
        self.assertRedirects(response, reverse('invalid-payment', kwargs={'invalid_id': 5}), target_status_code=200)
        print("400, OK")

    def assert_login_redirect(self, next_page, response):
        """Checks whether user was redirected to login page because he was unauthorized"""
        login_url = reverse('login')
        url_string = login_url + "?next=" + next_page
        self.assertRedirects(response, url_string, target_status_code=200)
