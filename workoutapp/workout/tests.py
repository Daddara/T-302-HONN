from django.test import TestCase, Client
from django.urls import reverse


class CreateWorkoutTest(TestCase):
    def init(self):
        self.client = Client()

    def test_create_view_get(self):
        print("Testing create workout page: ", end="")
        response = self.client.get(reverse('create workout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout/create_workout.html')
        print("200, OK")
