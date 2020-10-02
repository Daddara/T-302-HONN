from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from workout.models import Workout, Exercise, WorkoutRating, ExerciseRating
from django.contrib.auth.decorators import login_required


# Create your views here.
def placeholder_home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'user/placeholder_page.html')


def dashboard(request):
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
