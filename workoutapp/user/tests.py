import json

from django.http import HttpResponse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from user.models import Follow, UserInfo, FriendRequest


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

    def test_profile_page(self):
        print("Testing profile page: ", end="")
        data = {'username': 'TestUser',
                'email': 'test_user@test.com',
                'password1': 'iampassword', 'password2': 'iampassword'}
        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, reverse('login'), target_status_code=200)
        if User.objects.filter(username=data['username']).exists():
            login_data = {'username': data['username'], 'password': data['password1']}
            response = self.client.post(reverse('login'), data=login_data, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'dashboard/dashboard_workout.html')
            response = self.client.get(reverse('profile', kwargs={'slug': data['username']}))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'user/profile.html')
            print("200, OK")

    def test_profile_edit_get(self):
        print("Testing profile page edit (get): ", end="")
        data = {'username': 'TestUser',
                'email': 'test_user@test.com',
                'password1': 'iampassword', 'password2': 'iampassword'}
        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, reverse('login'), target_status_code=200)
        if User.objects.filter(username=data['username']).exists():
            self.client.login(username="TestUser", password="iampassword")
            response = self.client.get(reverse('edit-user'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'user/edit_profile.html')
            print("200, OK")

    def test_profile_edit_post(self):
        print("Testing profile page edit (post): ", end="")
        user_data = {'username': 'TestUser',
                     'email': 'test_user@test.com',
                     'password1': 'iampassword', 'password2': 'iampassword'}
        # Create user
        self.client.post(reverse('register'), user_data)

        # Get user
        user = User.objects.get(username=user_data['username'])

        # Login
        self.client.login(username="TestUser", password="iampassword")

        # Set up data to insert into form
        mod_user_info = {'first_name': 'New first name',
                         'last_name': 'New last name',
                         'birth_date': '1969-04-20',
                         'email': 'test_user@test.com',
                         'bio': 'blabla',
                         'profile_image': 'newimageurl',
                         'cover_image': 'new_cover_image'}
        # Post the data
        response = self.client.post(reverse('edit-user'), mod_user_info)

        # Check that it redirected to profile (happens on success)
        self.assertRedirects(response, reverse('profile', kwargs={'slug': user.username}), target_status_code=200)

        # Get the user info and check that it changed
        users_info = UserInfo.objects.get(user=user)
        self.assertEqual(users_info.first_name, mod_user_info['first_name'])
        print("200, OK")


class FollowTest(TestCase):
    def setUp(self):
        # Initialize client
        self.client = Client()
        # Create user
        data = {'username': 'TestUser',
                'email': 'test_user@test.com',
                'password1': 'iampassword', 'password2': 'iampassword'}
        data2 = {'username': 'TestUser2',
                 'email': 'test_user@test.com',
                 'password1': 'iampassword2', 'password2': 'iampassword2'}
        response = self.client.post(reverse('register'), data)
        response = self.client.post(reverse('register'), data2)
        self.assertRedirects(response, '/accounts/login/', target_status_code=200)
        self.user = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.assertEqual(self.user.username, 'TestUser')
        self.client.login(username="TestUser", password="iampassword")

    def test_following_view_get(self):
        self.follow = Follow.objects.create(Username=self.user, Following=self.user2)
        print("Testing following page: ", end="")
        response = self.client.get(reverse('following'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/followerlist.html')
        print("200, OK")

    def is_following_test(self):
        self.follow = Follow.objects.create(Username=self.user, Following=self.user2)
        print("Testing if he follows: ", end="")
        follow = Follow.objects.get(Following=self.user2)
        self.assertEqual(follow, pk=2)
        print("200, OK")

    def test_follow(self):
        print("Testing follow request: ", end="")
        response = self.client.get(reverse('follow'), data={'user_id': self.user2.id})
        self.assertJSONEqual(response.content, {'msg': 'Successfully followed user'})

    def test_search_result_view_get_search(self):
        self.follow = Follow.objects.create(Username=self.user, Following=self.user2)
        print("Testing search filter response: ", end="")
        response = self.client.get(reverse('search-user'), data={'search_input': 'TestUser2'})
        self.assertEqual(response.status_code, 200)
        print("200, OK")


class FriendsTest(TestCase):
    def setUp(self):
        # Initialize client
        self.client = Client()

        # Create user
        data = {'username': 'TestUser',
                'email': 'test_user@test.com',
                'password1': 'iampassword', 'password2': 'iampassword'}
        data2 = {'username': 'TestUser2',
                 'email': 'test_user@test.com',
                 'password1': 'iampassword2', 'password2': 'iampassword2'}
        response = self.client.post(reverse('register'), data)
        response = self.client.post(reverse('register'), data2)
        self.assertRedirects(response, reverse('login'), target_status_code=200)
        self.user = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user_info = UserInfo.objects.get(user=self.user)
        self.user_info2 = UserInfo.objects.get(user=self.user2)
        self.assertEqual(self.user.username, 'TestUser')
        self.client.login(username="TestUser", password="iampassword")

    def test_friend_list_view_get(self):
        print("Testing following page: ", end="")
        response = self.client.get(reverse('user_friends'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_friends.html')
        print("200, OK")

    def test_new_friend_request(self):
        print("Testing if friend request is created: ", end="")
        # friend_request = FriendRequest.objects.create(FromUser=self.user, ToUser=self.user2)
        response = self.client.get('/accounts/friend-request/send/2')
        self.assertEqual(len(FriendRequest.objects.all()), 1)
        find_request = FriendRequest.objects.get(FromUser=self.user, ToUser=self.user2)
        self.assertEqual(find_request.ToUser, self.user2)
        self.assertEqual(find_request.FromUser, self.user)
        print("200, OK")

    def test_cancel_friend_request(self):
        print("Testing friend request cancel: ", end="")
        friend_request = FriendRequest.objects.create(FromUser=self.user, ToUser=self.user2)
        self.assertEqual(len(FriendRequest.objects.all()), 1)

        response = self.client.get('/accounts/friend-request/cancel/2')
        self.assertEqual(len(FriendRequest.objects.all()), 0)
        self.assertNotIn(self.user_info, self.user_info2.friends.all())
        print("200, OK")

    def test_accept_friend_request(self):
        print("Testing friend request accept: ", end="")
        friend_request = FriendRequest.objects.create(FromUser=self.user2, ToUser=self.user)
        self.assertEqual(len(FriendRequest.objects.all()), 1)

        response = self.client.get('/accounts/friend-request/accept/2')
        self.assertEqual(len(FriendRequest.objects.all()), 0)
        self.assertIn(self.user_info2, self.user_info.friends.all())
        print("200, OK")

    def test_delete_friend_request(self):
        print("Testing friend request delete: ", end="")
        friend_request = FriendRequest.objects.create(FromUser=self.user2, ToUser=self.user)
        self.assertEqual(len(FriendRequest.objects.all()), 1)

        response = self.client.get('/accounts/friend-request/delete/2')
        self.assertEqual(len(FriendRequest.objects.all()), 0)
        self.assertNotIn(self.user_info2, self.user_info.friends.all())
        print("200, OK")
