from django.test import TestCase, Client
from django.urls import reverse

from workout.models import Exercise, ExerciseRating, RatingValue, Workout, Category
from django.contrib.auth.models import User


class CreateWorkoutTest(TestCase):
    def init(self):
        self.client = Client()

    def test_create_view_get_not_logged_in(self):
        print("Testing create workout unauthorized: ", end="")
        response = self.client.get(reverse('create workout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')
        print("200, OK")

class ViewWorkoutDetailsTest(TestCase):
    def init(self):
        self.client = Client()

    def test_get_workout_details_view(self):
        print("Testing get workout details unauthorized: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        category = Category.objects.create(Name="Penis")
        workout = Workout.objects.create(User=test_user, Name="Test Workout", Public=True, Category=category)
        response = self.client.get(reverse('workout_details', kwargs={'workout_id': workout.id}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout/workout_details.html')
        print("200, OK")


class RateExerciseTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        self._setup_user()
        self.user1 = User.objects.get(pk=1)
        
        self._setup_exercise()
        self.exercise1 = Exercise.objects.get(pk=1)

    def _setup_user(self):
        data1 = {'username': 'TestUser',
                'email': 'test_user@test.com',
                'password1': 'iampassword', 'password2': 'iampassword'}
        self.client.post(reverse('register'), data1)
        
    def _setup_exercise(self):
        Exercise(
            Public=True,
            Title="I'm super tired",
            Creator=self.user1).save()
    
    def test_post_like(self):
        self.client.force_login(self.user1)
        response = self.client.post('/workout/rate_exercise', {'exercise_id': self.exercise1.id, 'rating': "+1"})
        self.assertEqual(response.status_code, 200)
        try:
            rating = ExerciseRating.objects.get(Judge=self.user1, Exercise=self.exercise1)
            self.assertEqual(rating.Judge, self.user1)
            self.assertEqual(rating.Exercise, self.exercise1)
            self.assertEqual(rating.Rating, 1)
        except ExerciseRating.DoesNotExist:
            self.assertTrue(False)
    
    def test_update_dislike(self):
        self.client.force_login(self.user1)
        response1 = self.client.post('/workout/rate_exercise', {'exercise_id': self.exercise1.id, 'rating': "+1"})
        self.assertEqual(response1.status_code, 200)
        try:
            rating = ExerciseRating.objects.get(Judge=self.user1, Exercise=self.exercise1)
        except ExerciseRating.DoesNotExist:
            self.assertTrue(False)

        self.client.force_login(self.user1)
        response2 = self.client.post('/workout/rate_exercise', {'exercise_id': self.exercise1.id, 'rating': "-1"})
        self.assertEqual(response2.status_code, 200)
        try:
            rating = ExerciseRating.objects.get(Judge=self.user1, Exercise=self.exercise1)
            self.assertEqual(rating.Judge, self.user1)
            self.assertEqual(rating.Exercise, self.exercise1)
            self.assertEqual(rating.Rating, -1)
        except ExerciseRating.DoesNotExist:
            self.assertTrue(False)
    
    def test_fails(self):
        # Unauthorized
        response1 = self.client.post('/workout/rate_exercise', {'exercise_id': self.exercise1.id, 'rating': "+1"})
        self.assertEqual(response1.status_code, 401)

        # invalid
        self.client.force_login(self.user1)
        response1 = self.client.post('/workout/rate_exercise', {'exercise_id': self.exercise1.id, 'rating': "17"})
        self.assertEqual(response1.status_code, 400)
        response1 = self.client.post('/workout/rate_exercise', {'exercise_id': "Me", 'rating': "+1"})
        self.assertEqual(response1.status_code, 400)
        
        # Exercise not found
        response1 = self.client.post('/workout/rate_exercise', {'exercise_id': 21921212, 'rating': "+1"})
        self.assertEqual(response1.status_code, 404)
