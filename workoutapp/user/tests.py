from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class UserViewTests(TestCase):
    def init(self):

        self.client = Client()

    def test_register_view_get(self):

        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/register.html')

    def test_register_view_post(self):
        data = {'username': 'TestUser',
               'email': 'test_user@test.com',
               'password1': 'iampassword', 'password2': 'iampassword'}

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/')

        user = False
        if User.objects.filter(username=data['username']).exists():
            user = True
            print(user)
        self.assertTrue(user)
