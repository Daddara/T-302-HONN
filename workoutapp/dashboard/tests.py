from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from .views import creation_time_passed
import datetime

# Create your tests here.
class UserViewTests(TestCase):
    def init(self):
        self.client = Client()

    def test_dashboard_view_get(self):
        print("Testing dashboard page: ", end="")
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')
        print("200, OK")

    def test_public_workout_view_get(self):
        print("Testing workouts page: ", end="")
        response = self.client.get(reverse('public_workouts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/public_workouts.html')
        print("200, OK")

    def test_public_exercise_view_get(self):
        print("Testing Exercises page: ", end="")
        response = self.client.get(reverse('public_exercises'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/public_exercises.html')
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