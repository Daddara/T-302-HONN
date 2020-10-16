from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from workout.models import Exercise

import datetime

from workout.models import Workout
from dashboard.views import creation_time_passed, get_workouts_with_likes

# Create your tests here.
class UserViewTests(TestCase):
    def init(self):
        self.client = Client()

    def test_dashboard_view(self):
        print("Testing dashboard page: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        self.client.login(username="TestUser", password="iampassword")
        response = self.client.get(reverse('dashboard'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')
        print("200, OK")

    def test_dashboard_view_get_unauthenticated(self):
        print("Testing dashboard unauthenticated: ", end="")
        response = self.client.get(reverse('dashboard'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')
        print("200, OK")

    def test_get_created_exercises(self):
        print("Testing created exercises: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        data = {'Creator': test_user}
        if Exercise.objects.filter(Creator=data['Creator']).exists():
            response = self.client.get(reverse('dashboard'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'dashboard/dashboard.html')
            print("200, OK")

    def test_get_created_workouts(self):
        print("Testing created workouts: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        data = {'User': test_user}
        if Workout.objects.filter(User=data['User']).exists():
            response = self.client.get(reverse('dashboard'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'dashboard/dashboard.html')
            print("200, OK")

    def test_public_workout_view_get(self):
        print("Testing workouts page: ", end="")
        response = self.client.get(reverse('public_workouts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_workout.html')
        print("200, OK")

    def test_public_exercise_view_get(self):
        print("Testing Exercises page: ", end="")
        response = self.client.get(reverse('public_exercises'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_exercise.html')
        print("200, OK")
    
    def test_creation_time_passed(self):
        print("Testing exercise creation time: ", end="")
        
        class DummyData:
            def __init__(self, time):
                self.CreatedAt = time

        data = DummyData(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=15))
        data = creation_time_passed(data)
        self.assertEqual(data.time_passed, "15 min ago")

        data = DummyData(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=3))
        data = creation_time_passed(data)
        self.assertEqual(data.time_passed, "3 hours ago")

        data = DummyData(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=2))
        data = creation_time_passed(data)
        self.assertEqual(data.time_passed, "2 days ago")

        data = DummyData(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=9))
        data = creation_time_passed(data)
        self.assertEqual(data.time_passed, "1 weeks ago")

        data = DummyData(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(weeks=9))
        data = creation_time_passed(data)
        self.assertEqual(data.time_passed, "2 months ago")

        data = DummyData(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(weeks=130))
        data = creation_time_passed(data)
        self.assertEqual(data.time_passed, "3 years ago")

    def test_get_workouts_with_likes(self):
        self._setup_user()
        user1 = User.objects.get(pk=1)
        
        self._setup_workout(user1)

        self.client.force_login(user1)
        user1 = User.objects.get(pk=1)
        workout = Workout.objects.get(pk=1)
        response = self.client.post(reverse('rate_workout'), {'exercise_id': workout.id, 'rating': "+1"})

        response = self.client.post(reverse('public_exercises'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_exercise.html')
        print("200, OK")

    def _setup_user(self):
        data1 = {'username': 'TestUser',
                'email': 'test_user@test.com',
                'password1': 'iampassword', 'password2': 'iampassword'}
        self.client.post(reverse('register'), data1)
        
    def _setup_workout(self, user1):
        Workout(
            Name="iNSaNiTY",
            User=user1,
            short_description="I don't know who I am").save()