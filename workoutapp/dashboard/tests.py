from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from workout.models import Exercise

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

    def test_get_created_exercises(self):
        print("Testing created exercises: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        data = {'Creator': test_user}
        if Exercise.objects.filter(Creator=data['Creator']).exists():
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