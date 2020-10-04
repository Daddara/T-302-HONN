from django.contrib.auth.models import User
from django.test import TestCase, Client


# Create your tests here.
from django.urls import reverse

from payment.models import Product
from wallet.models import Wallet


# noinspection DuplicatedCode
class TestWallet(TestCase):
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

    def test_create_view_get(self):
        print("Testing that wallet returns a view", end="")
        response = self.client.get(reverse('wallet'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wallet/wallet.html')
        print("200, OK")

    def tearDown(self):
        # Clean up run after every test method.
        self.client.logout()

    def test_wallet_existence(self):
        print("Testing if wallet exists: ", end="")
        user_wallet = Wallet.objects.get(user=self.user)
        self.assertTrue(user_wallet)
        print("True, OK")

    def test_wallet_balance(self):
        print("Testing wallet balance: ", end="")
        wallet = Wallet.objects.get(user=self.user)
        wallet.add_balance(5000)
        self.assertEqual(wallet.fitcoin, 5000)
        print("200, OK")

    def test_wallet_funding(self):
        print("Testing wallet increase after purchase: ", end="")
        product_id = self.product.id
        response = self.client.get(reverse('test-payment', kwargs={'product_id': product_id, 'error_insertion': 0}))
        wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(wallet.fitcoin, 4000)
        print("200, OK")


