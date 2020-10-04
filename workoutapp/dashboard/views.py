from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from workout.models import Workout, Exercise, WorkoutRating, ExerciseRating
from django.contrib.auth.decorators import login_required
from datetime import timedelta, datetime
import pytz


# Create your views here.
def placeholder_home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'user/placeholder_page.html')


def dashboard(request):
    if request.user.is_authenticated:
        user_exercises = Exercise.objects.filter(Creator=request.user).values()
        return render(request, 'dashboard/dashboard.html', context={'user_exercises': user_exercises})
    else:
        return render(request, 'dashboard/dashboard.html')

def workouts(request):
    context = {'workouts': get_workouts_with_likes(request)}
    return render(request, 'dashboard/public_workouts.html', context)


def exercises(request):
    context = {'exercises': get_exercises_with_likes(request)}
    return render(request, 'dashboard/public_exercises.html', context)


def get_exercises_with_likes(request):
    # KEEP IN MIND ALL THE CHANGES THAT ARE MADE IN THIS MODEL ARE NOT SAVED TO DB
    # ONLY MODIFIED FOR THE FRONT END
    exercise_models = None
    try:
        exercise_models = Exercise.objects.filter(Public=True)
    except Exercise.DoesNotExist:
        return None

    if exercise_models:
        for model in exercise_models:
            # Get the count of all likes on current exercise
            try:
                likes = ExerciseRating.objects.filter(Exercise=model, Rating=1).count()
            except ExerciseRating.DoesNotExist:
                likes = 0
            # Get the count of all dislikes on current exercise
            try:
                dislikes = ExerciseRating.objects.filter(Exercise=model, Rating=-1).count()
            except ExerciseRating.DoesNotExist:
                dislikes = 0

            # Edit the values in the model instance (only for front end, not doing a model.save())
            model.Likes = likes
            model.Dislikes = dislikes

            # If the user is logged in we want to show him if he liked something
            if request.user.is_authenticated:
                try:
                    # Trying to fetch a user rating model instance on the current exercise
                    user_rating = ExerciseRating.objects.get(Exercise=model, Judge=request.user)
                except ExerciseRating.DoesNotExist:
                    # Set as none if it cannot be found
                    user_rating = None

                # If the user has rated this exercise
                if user_rating:
                    # If the user liked the exercise
                    if user_rating.Rating == 1:
                        model.Has_Liked = True
                    # If the user disliked the exercise
                    elif user_rating.Rating == -1:
                        model.Has_Disliked = True

        return exercise_models


def get_workouts_with_likes(request):
    workout_models = None
    try:
        workout_models = Workout.objects.filter(Public=True)
    except Workout.DoesNotExist:
        return None

    if workout_models:
        for model in workout_models:
            model = creation_time_passed(model)
            # Get the count of all likes on current exercise
            try:
                likes = WorkoutRating.objects.filter(Workout=model, Rating=1).count()
            except WorkoutRating.DoesNotExist:
                likes = 0
            # Get the count of all dislikes on current exercise
            try:
                dislikes = WorkoutRating.objects.filter(Workout=model, Rating=-1).count()
            except WorkoutRating.DoesNotExist:
                dislikes = 0

            # Edit the values in the model instance (only for front end, not doing a model.save())
            model.Likes = likes
            model.Dislikes = dislikes

            # If the user is logged in we want to show him if he liked something
            if request.user.is_authenticated:
                try:
                    # Trying to fetch a user rating model instance on the current exercise
                    user_rating = WorkoutRating.objects.get(Workout=model, Judge=request.user)
                except WorkoutRating.DoesNotExist:
                    # Set as none if it cannot be found
                    user_rating = None

                # If the user has rated this exercise
                if user_rating:
                    # If the user liked the exercise
                    if user_rating.Rating == 1:
                        model.Has_Liked = True
                    # If the user disliked the exercise
                    elif user_rating.Rating == -1:
                        model.Has_Disliked = True

        return workout_models


def creation_time_passed(workout_model):
    date_time_now = datetime.now()
    timezone = pytz.timezone("UCT")
    date_time_now = timezone.localize(date_time_now)
    time_diff = date_time_now - workout_model.CreatedAt
    time_delta = time_diff.total_seconds()
    minutes = time_delta / 60
    time_passed_value = round(minutes)
    time_passed_unit = "min"
    if minutes >= 60:
        hours = time_delta / 3600
        time_passed_unit = "hours"
        time_passed_value = round(hours)
        if hours >= 24:
            days = time_delta / 3600 * 24
            time_passed_unit = "days"
            time_passed_value = round(days)
            if days >= 7:
                weeks = time_delta / 3600 * 24 * 7
                time_passed_unit = "weeks"
                time_passed_value = round(weeks)
                if weeks >= 4:
                    months = time_delta / 3600 * 24 * 30
                    time_passed_unit = "months"
                    time_passed_value = round(months)
                    if months >= 12:
                        years = time_delta / 3600 * 24 * 365
                        time_passed_unit = "years"
                        time_passed_value = round(years)

    time_passed_string = '{} {} ago'.format(time_passed_value, time_passed_unit)
    workout_model.time_passed = time_passed_string
    return workout_model
