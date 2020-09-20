from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from user.models import Follow

# Create your tests here.
class UserViewTests(TestCase):
    def init(self):
        self.client = Client()

    def test_register_view_get(self):
        print("Testing registration page: ", end="")
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/register.html')
        print("200, OK")

    def test_register_view_post(self):
        print("Testing user registration: ", end="")
        data = {'username': 'TestUser',
               'email': 'test_user@test.com',
               'password1': 'iampassword', 'password2': 'iampassword'}

        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, reverse('login'), target_status_code=200)
        user = False
        if User.objects.filter(username=data['username']).exists():
            user = True
        self.assertTrue(user)
        print("201, OK")

    def test_invalid_register(self):
        """Creating a user, then trying to create another user with the same username.
        Should load registration page again with form errors"""
        User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        print("Testing invalid registration: ", end="")
        data = {'username': 'TestUser',
                'email': 'test_user@test.com',
                'password1': 'iampassword', 'password2': 'iampassword'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        print("200, OK")

    def test_following_view_get(self):
        print("Testing following page: ", end="")
        response = self.client.get(reverse('following'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/followerlist.html')
        print("200, OK")


