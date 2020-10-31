from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from workout.models import Exercise, MuscleGroup, Category, ExerciseRating, WorkoutRating

import datetime

from workout.models import Workout
from dashboard.views import creation_time_passed, get_workouts_with_likes


# Create your tests here.
class UserViewTests(TestCase):
    # The missing coverage is just error prevetion code...
    def init(self):
        self.client = Client()

    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('public_workouts'))

    def test_workouts_view(self):
        print("Testing public workout dashboard: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        category = Category.objects.create(Name="Penis")
        new_workout = Workout.objects.create(User=test_user, Name="Test Workout", Public=True, Category=category)
        WorkoutRating.objects.create(Workout=new_workout, Judge=test_user)
        self.client.login(username="TestUser", password="iampassword")
        response = self.client.get(reverse('public_workouts'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_workout.html')
        print("200, OK")

    def test_user_workout_view(self):
        print("Testing private workout dashboard: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        self.client.login(username="TestUser", password="iampassword")
        response = self.client.get(reverse('user_workouts'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_workout.html')
        print("200, OK")

    def test_user_exercise_view_unauthenticated(self):
        print("Testing private exercise dashboard unauthenticated: ", end="")
        response = self.client.get(reverse('user_exercises'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')
        print("200, OK")

    def test_user_exercise_view(self):
        print("Testing private exercise dashboard: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        muscle_group = MuscleGroup.objects.create(name="Penis")
        exercise = Exercise.objects.create(Title="Test", Creator=test_user, muscle_group=muscle_group, Public=True)
        ExerciseRating.objects.create(Judge=test_user, Exercise=exercise)
        self.client.login(username="TestUser", password="iampassword")
        response = self.client.get(reverse('user_exercises'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_exercise.html')
        print("200, OK")

    def test_exercises_view(self):
        print("Testing public exercise dashboard: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        muscle_group = MuscleGroup.objects.create(name="Penis")
        exercise = Exercise.objects.create(Title="Test", Creator=test_user, muscle_group=muscle_group, Public=True)
        ExerciseRating.objects.create(Judge=test_user, Exercise=exercise)
        self.client.login(username="TestUser", password="iampassword")
        response = self.client.get(reverse('public_exercises'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_exercise.html')
        print("200, OK")

    def test_filter_exercises(self):
        muscle_group = MuscleGroup.objects.create(name="Penis")
        print("Testing category filter in public exercises: ", end="")
        response = self.client.get(reverse('public-filter-e', kwargs={'muscle_group': muscle_group.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_exercise.html')
        print("200, OK")

    def test_filter_workouts(self):
        category = Category.objects.create(Name="Penis")
        print("Testing category filter in public workouts: ", end="")
        response = self.client.get(reverse('public-filter-w', kwargs={'category_id': category.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_workout.html')
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

    def test_favourite_exercise_view(self):
        print("Testing favourite exercise view: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        self.client.login(username="TestUser", password="iampassword")
        response = self.client.get(reverse('favourite_exercise'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_favourites_exercise.html')
        print("200, OK")

    def test_favourites_add_exercise(self):

        pass

    def test_favourites_remove_exercise(self):

        pass

    def test_favourites_add_exercise_unauthenticated(self):
        print("Testing adding favourite exercise unauthenticated: ", end="")
        response = self.client.get(reverse('favourites_add_exercise'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/register.html')
        print("200, OK")

    def test_favourite_workout_view(self):
        print("Testing favourite workout view: ", end="")
        test_user = User.objects.create_user(username="TestUser", password="iampassword", email="randomemail@gmail.com")
        self.client.login(username="TestUser", password="iampassword")
        response = self.client.get(reverse('favourite_workout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard_favourites_workout.html')
        print("200, OK")

    def test_favourites_add_workout(self):

        pass

    def test_favourites_remove_workout(self):

        pass

    def test_favourites_add_workout_unauthenticated(self):
        print("Testing adding favourite workout unauthenticated: ", end="")
        response = self.client.get(reverse('favourites_add_workout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/register.html')
        print("200, OK")