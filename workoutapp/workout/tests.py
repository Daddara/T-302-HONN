from django.test import TestCase, Client
from django.urls import reverse
from workout.models import Exercise, ExerciseRating, RatingValue, Category, Workout, Equipment, MuscleGroup, WorkoutRating
from django.contrib.auth.models import User


class CreateWorkoutTest(TestCase):
    def init(self):
        self.client = Client()

    def test_create_view_get_not_logged_in(self):
        print("Testing create workout unauthorized get: ", end="")
        response = self.client.get(reverse('create workout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')
        print("200, OK")

    def _setup_user(self):
        data1 = {'username': 'TestUser',
                 'email': 'test_user@test.com',
                 'password1': 'iampassword', 'password2': 'iampassword'}
        self.client.post(reverse('register'), data1)
        self.client.login(username="TestUser", password="iampassword")

    def test_create_workout_view_get(self):
        self._setup_user()
        print("Testing workout creation page get: ", end="")
        response = self.client.get(reverse('create workout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout/create_workout.html')
        print("200, OK")

    def test_create_workout_post(self):
        self._setup_user()
        print("Testing workout creation POST request: ", end="")
        Category(Name="Strength Training").save()
        category = Category.objects.get(id=1)
        data = {
            'Name': "Test Workout",
            'Category': category.id,
            'Image': "https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png",
            'short_description': "Just a liddle test workout :)",
            'workout_goal': "Big Strong"
        }
        response = self.client.post(reverse('create workout'), data, follow=True)
        workout = Workout.objects.get(Name="Test Workout")
        self.assertRedirects(response, reverse('add exercises', kwargs={'workout_id': workout.id}),
                             target_status_code=200)
        self.assertEqual(workout.workout_goal, data['workout_goal'])
        print("200, OK")


class CreateExerciseTest(TestCase):
    def setUp(self):
        self.client = Client()

    def _setup_user(self):
        self.user = {'username': 'TestUser',
                     'email': 'test_user@test.com',
                     'password1': 'iampassword', 'password2': 'iampassword'}
        self.client.post(reverse('register'), self.user)
        self.client.login(username="TestUser", password="iampassword")

    def test_create_view_get_not_logged_in(self):
        print("Testing create workout unauthorized: ", end="")
        response = self.client.get(reverse('create workout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')
        print("200, OK")

    def test_create_exercise_view_get(self):
        self._setup_user()
        print("Testing workout creation page: ", end="")
        response = self.client.get(reverse('create exercise'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exercise/create_exercise.html')
        print("200, OK")

    def test_exercise_creation_post(self):
        self._setup_user()
        user = User.objects.get(username=self.user['username'])
        Equipment(
            Name="Running Shoes",
            Description="Shoes comfortable to run in"
        ).save()
        MuscleGroup(name="Legs").save()

        print("Testing workout creation: ", end="")
        equipment = Equipment.objects.get(pk=1)
        muscle_group = MuscleGroup.objects.get(pk=1)
        data = {
            'Title': "Test Exercise",
            'Description': "Just a liddle test exercise :)",
            'Image': "https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png",
            'Equipment': equipment.id,
            'muscle_group': muscle_group.id,
            'Public': False
        }
        response = self.client.post(reverse('create exercise'), data, follow=True)
        self.assertRedirects(response, reverse('profile', kwargs={'slug': user.username}), target_status_code=200)
        exercise = Exercise.objects.get(Title=data['Title'])
        self.assertEqual(exercise.Description, data['Description'])
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
        print("Testing exercise like POST: ", end="")
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
        print("200, OK")

    def test_update_dislike(self):
        print("Testing exercise dislike: ", end="")
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
        print("200, OK")

    def test_fails(self):
        print("Testing exercise like fails: ", end="")
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
        print("200, OK")


class RateWorkoutTest(TestCase):
    def setUp(self):
        self.client = Client()

        self._setup_user()
        self.user1 = User.objects.get(pk=1)

        self._setup_workout()
        self.workout1 = Workout.objects.get(pk=1)

    def _setup_user(self):
        data1 = {'username': 'TestUser',
                 'email': 'test_user@test.com',
                 'password1': 'iampassword', 'password2': 'iampassword'}
        self.client.post(reverse('register'), data1)

    def _setup_workout(self):
        Category(Name="Strength Training").save()
        category = Category.objects.get(id=1)
        Workout(
            User=self.user1,
            Name="Test Workout",
            Category=category,
            Image="https://www.vhv.rs/dpng/d/256-2569650_men-profile-icon-png-image-free-download-searchpng.png",
            short_description="Just a liddle test workout :)",
            workout_goal="Big Strong").save()

    def test_post_like(self):
        print("Testing workout like POST: ", end="")
        self.client.force_login(self.user1)
        response = self.client.post('/workout/rate_workout', {'workout_id': self.workout1.id, 'rating': "+1"})
        self.assertEqual(response.status_code, 200)
        try:
            rating = WorkoutRating.objects.get(Judge=self.user1, Workout=self.workout1)
            self.assertEqual(rating.Judge, self.user1)
            self.assertEqual(rating.Workout, self.workout1)
            self.assertEqual(rating.Rating, 1)
        except WorkoutRating.DoesNotExist:
            self.assertTrue(False)
        print("200, OK")

    def test_update_dislike(self):
        print("Testing workout dislike: ", end="")
        self.client.force_login(self.user1)
        response1 = self.client.post('/workout/rate_workout', {'workout_id': self.workout1.id, 'rating': "+1"})
        self.assertEqual(response1.status_code, 200)
        try:
            rating = WorkoutRating.objects.get(Judge=self.user1, Workout=self.workout1)
        except WorkoutRating.DoesNotExist:
            self.assertTrue(False)

        self.client.force_login(self.user1)
        response2 = self.client.post('/workout/rate_workout', {'workout_id': self.workout1.id, 'rating': "-1"})
        self.assertEqual(response2.status_code, 200)
        try:
            rating = WorkoutRating.objects.get(Judge=self.user1, Workout=self.workout1)
            self.assertEqual(rating.Judge, self.user1)
            self.assertEqual(rating.Workout, self.workout1)
            self.assertEqual(rating.Rating, -1)
        except WorkoutRating.DoesNotExist:
            self.assertTrue(False)
        print("200, OK")

    def test_fails(self):
        print("Testing workout like fail: ", end="")
        # Unauthorized
        response1 = self.client.post('/workout/rate_workout', {'workout_id': self.workout1.id, 'rating': "+1"})
        self.assertEqual(response1.status_code, 401)

        # invalid
        self.client.force_login(self.user1)
        response1 = self.client.post('/workout/rate_workout', {'workout_id': self.workout1.id, 'rating': "17"})
        self.assertEqual(response1.status_code, 400)
        response1 = self.client.post('/workout/rate_workout', {'workout_id': "Me", 'rating': "+1"})
        self.assertEqual(response1.status_code, 400)

        # Exercise not found
        response1 = self.client.post('/workout/rate_workout', {'workout_id': 21921212, 'rating': "+1"})
        self.assertEqual(response1.status_code, 404)
        print("200, OK")
